# FILE NAME: app.py
# FILE PATH: backend/app.py
# PURPOSE: FastAPI application entry point, database setup, and REST API routing.

import sqlite3
import uuid
import os
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Any

app = FastAPI(
    title="Social Media Privacy Risk Assessment Framework API",
    version="1.0.0",
    description="Defensive privacy-risk evaluation and posture hardening engine."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "data/privacy_framework.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessments (
            assessment_id TEXT PRIMARY KEY,
            overall_score REAL,
            risk_level TEXT,
            created_at TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS category_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id TEXT,
            category TEXT,
            score REAL,
            FOREIGN KEY(assessment_id) REFERENCES assessments(assessment_id)
        )
    """)
    
    conn.commit()
    conn.close()

init_db()

class AssessmentRequest(BaseModel):
    responses: Dict[str, Any]

class SimulationRequest(BaseModel):
    current_score: float
    improvements: List[str]

CATEGORY_MAPPING = {
    "Profile Visibility": ["profile_visibility", "search_engine_indexing", "friends_list_public"],
    "Personal Information": ["phone_public", "email_public", "birthday_public", "workplace_public"],
    "Location Privacy": ["location_public", "travel_posts", "realtime_checkins", "home_location_exposed"],
    "Posts & Content": ["posts_public", "historical_posts_public", "photo_metadata_exposed", "archived_posts_shared"],
    "Connections": ["unknown_connections", "connection_limit_disabled", "public_follower_count"],
    "Tagging": ["tagging_anyone_allowed", "tag_review_disabled", "mention_unknown_allowed"],
    "Account Security": ["mfa_enabled", "password_reuse_reported", "login_alerts_enabled", "weak_recovery_info"],
    "Third-Party Apps": ["third_party_apps_reviewed", "untrusted_oauth_granted", "stale_integrations_active"],
    "Social Engineering": ["suspicious_link_awareness", "dm_from_unknowns", "giveaway_participation"],
    "Digital Footprint": ["old_accounts_active", "public_comments_indexed", "privacy_settings_reviewed"]
}

CATEGORY_WEIGHTS = {
    "Profile Visibility": 0.10,
    "Personal Information": 0.15,
    "Location Privacy": 0.15,
    "Posts & Content": 0.10,
    "Connections": 0.05,
    "Tagging": 0.05,
    "Account Security": 0.15,
    "Third-Party Apps": 0.05,
    "Social Engineering": 0.15,
    "Digital Footprint": 0.10
}

@app.post("/api/assessment")
def submit_assessment(payload: AssessmentRequest):
    from services.scoring_engine import calculate_category_score, compute_overall_risk
    from services.recommendation_engine import generate_findings_and_recommendations
    
    responses = payload.responses
    assessment_id = str(uuid.uuid4())
    created_at = datetime.utcnow().isoformat()
    
    category_scores = {}
    for cat_name, keys in CATEGORY_MAPPING.items():
        category_scores[cat_name] = calculate_category_score(responses, keys, {k: 1.0 for k in keys})
        
    overall_score, risk_level = compute_overall_risk(category_scores, CATEGORY_WEIGHTS)
    findings, recommendations = generate_findings_and_recommendations(responses)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO assessments (assessment_id, overall_score, risk_level, created_at) VALUES (?, ?, ?, ?)",
        (assessment_id, overall_score, risk_level, created_at)
    )
    for cat, score in category_scores.items():
        cursor.execute(
            "INSERT INTO category_scores (assessment_id, category, score) VALUES (?, ?, ?)",
            (assessment_id, cat, score)
        )
    conn.commit()
    conn.close()
    
    return {
        "assessment_id": assessment_id,
        "created_at": created_at,
        "overall_score": overall_score,
        "risk_level": risk_level,
        "category_scores": category_scores,
        "findings": findings,
        "recommendations": recommendations,
        "disclaimer": "Educational risk framework. Does not guarantee account security."
    }

@app.post("/api/assessment/simulate-improvement")
def simulate_improvement_endpoint(payload: SimulationRequest):
    from services.improvement_simulator import simulate_improvements
    return simulate_improvements(payload.current_score, payload.improvements)

@app.get("/api/dashboard/stats")
def get_dashboard_stats():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*), AVG(overall_score) FROM assessments")
    row = cursor.fetchone()
    total_assessments = row[0] or 0
    avg_score = round(row[1] or 0.0, 2)
    
    cursor.execute("SELECT risk_level, COUNT(*) FROM assessments GROUP BY risk_level")
    distribution = dict(cursor.fetchall())
    conn.close()
    
    return {
        "total_assessments": total_assessments,
        "average_risk_score": avg_score,
        "risk_distribution": distribution
    }
