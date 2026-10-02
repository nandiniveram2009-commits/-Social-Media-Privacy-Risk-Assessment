# FILE NAME: test_framework.py
# FILE PATH: tests/test_framework.py
# PURPOSE: Comprehensive pytest suite validating scoring, recommendations, and simulation engines.

import pytest
from backend.services.scoring_engine import calculate_category_score, compute_overall_risk
from backend.services.recommendation_engine import generate_findings_and_recommendations
from backend.services.improvement_simulator import simulate_improvements

def test_fully_private_profile():
    responses = {
        "profile_visibility": "PRIVATE",
        "phone_public": "NO",
        "email_public": "NO",
        "birthday_public": "NO",
        "mfa_enabled": "YES"
    }
    score = calculate_category_score(responses, ["profile_visibility", "phone_public"], {"profile_visibility": 1.0, "phone_public": 1.0})
    assert score == 0.0

def test_fully_public_profile():
    responses = {
        "profile_visibility": "PUBLIC",
        "phone_public": "YES",
        "email_public": "YES"
    }
    score = calculate_category_score(responses, ["profile_visibility", "phone_public"], {"profile_visibility": 1.0, "phone_public": 1.0})
    assert score == 100.0

def test_overall_risk_calculation():
    cat_scores = {
        "Profile Visibility": 50.0,
        "Personal Information": 80.0,
        "Account Security": 50.0
    }
    weights = {
        "Profile Visibility": 0.3,
        "Personal Information": 0.4,
        "Account Security": 0.3
    }
    overall, level = compute_overall_risk(cat_scores, weights)
    assert overall == 61.0
    assert level == "HIGH"

def test_recommendation_generation():
    responses = {
        "profile_visibility": "PUBLIC",
        "phone_public": "YES",
        "mfa_enabled": "NO"
    }
    findings, recs = generate_findings_and_recommendations(responses)
    assert len(findings) >= 3
    assert len(recs) >= 3

def test_improvement_simulation():
    current = 75.0
    improvements = ["make_profile_private", "enable_mfa"]
    result = simulate_improvements(current, improvements)
    assert result["simulated_score"] < current
    assert result["risk_reduction_points"] == 35.0
    assert result["new_risk_level"] == "MODERATE"
