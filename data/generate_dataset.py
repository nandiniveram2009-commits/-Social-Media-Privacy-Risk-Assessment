# FILE NAME: generate_dataset.py
# FILE PATH: data/generate_dataset.py
# PURPOSE: Generates 1,000 synthetic privacy assessment records for analytics.

import os
import random
import csv

def generate_synthetic_data(num_records=1000, output_path="data/social_media_privacy_assessments.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    visibility_options = ["PUBLIC", "FRIENDS", "PRIVATE"]
    boolean_options = ["YES", "NO", "SOMETIMES", "NOT SURE"]
    
    headers = [
        "profile_id", "profile_visibility", "phone_public", "email_public",
        "birthday_public", "location_public", "workplace_public", "education_public",
        "relationship_public", "posts_public", "location_tagging", "travel_posts",
        "unknown_connections", "tag_review_enabled", "third_party_apps_reviewed",
        "mfa_enabled", "login_alerts_enabled", "password_reuse_reported",
        "suspicious_link_awareness", "old_posts_reviewed", "privacy_settings_reviewed",
        "risk_score", "risk_level"
    ]
    
    rows = []
    for i in range(1, num_records + 1):
        p_vis = random.choice(visibility_options)
        phone = random.choice(boolean_options)
        email = random.choice(boolean_options)
        bday = random.choice(boolean_options)
        loc_pub = random.choice(boolean_options)
        work = random.choice(boolean_options)
        edu = random.choice(boolean_options)
        rel = random.choice(boolean_options)
        posts = random.choice(visibility_options)
        loc_tag = random.choice(boolean_options)
        travel = random.choice(boolean_options)
        unknown_conn = random.choice(boolean_options)
        tag_rev = random.choice(boolean_options)
        app_rev = random.choice(boolean_options)
        mfa = random.choice(boolean_options)
        alerts = random.choice(boolean_options)
        pwd_reuse = random.choice(boolean_options)
        link_aware = random.choice(boolean_options)
        old_posts = random.choice(boolean_options)
        settings_rev = random.choice(boolean_options)
        
        score = 0
        if p_vis == "PUBLIC": score += 15
        elif p_vis == "FRIENDS": score += 5
        if phone == "YES": score += 15
        if email == "YES": score += 10
        if bday == "YES": score += 10
        if loc_pub == "YES": score += 15
        if travel == "YES": score += 10
        if unknown_conn == "YES": score += 10
        if mfa == "NO": score += 15
        if pwd_reuse == "YES": score += 10
        if app_rev == "NO": score += 5
        
        score += random.randint(-10, 10)
        score = max(0, min(100, score))
        
        if score <= 20: level = "LOW"
        elif score <= 40: level = "MODERATE"
        elif score <= 70: level = "HIGH"
        else: level = "CRITICAL"
        
        rows.append([
            f"SYNTH_USER_{i:04d}", p_vis, phone, email, bday, loc_pub,
            work, edu, rel, posts, loc_tag, travel, unknown_conn,
            tag_rev, app_rev, mfa, alerts, pwd_reuse, link_aware,
            old_posts, settings_rev, score, level
        ])
        
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
        
    print(f"[+] Successfully generated {num_records} synthetic records at '{output_path}'.")

if __name__ == "__main__":
    generate_synthetic_data()
