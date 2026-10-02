# FILE NAME: recommendation_engine.py
# FILE PATH: backend/services/recommendation_engine.py
# PURPOSE: Maps detected risk conditions to prioritized remediation steps.

def generate_findings_and_recommendations(responses: dict) -> tuple:
    findings = []
    recommendations = []
    
    if responses.get("profile_visibility") == "PUBLIC":
        findings.append({
            "category": "Profile Visibility",
            "finding": "Profile is publicly searchable and visible to unauthenticated web users.",
            "severity": "HIGH"
        })
        recommendations.append({
            "priority": "IMMEDIATE",
            "action": "Change profile visibility setting from 'Public' to 'Friends Only' or 'Private'."
        })
        
    if responses.get("phone_public") == "YES":
        findings.append({
            "category": "Personal Information",
            "finding": "Phone number is exposed publicly, increasing spam and SIM-swapping risks.",
            "severity": "CRITICAL"
        })
        recommendations.append({
            "priority": "IMMEDIATE",
            "action": "Remove public phone number display and restrict contact lookup permissions."
        })
        
    if responses.get("birthday_public") == "YES":
        findings.append({
            "category": "Personal Information",
            "finding": "Full birth date is exposed publicly, enabling identity theft vectors.",
            "severity": "HIGH"
        })
        recommendations.append({
            "priority": "IMPORTANT",
            "action": "Hide full birth date or restrict display to month/day only."
        })
        
    if responses.get("location_public") == "YES" or responses.get("travel_posts") == "YES":
        findings.append({
            "category": "Location Privacy",
            "finding": "Real-time location sharing or travel itineraries are publicly broadcasted.",
            "severity": "CRITICAL"
        })
        recommendations.append({
            "priority": "IMMEDIATE",
            "action": "Disable real-time location tagging and post vacation/travel updates only after returning."
        })
        
    if responses.get("mfa_enabled") != "YES":
        findings.append({
            "category": "Account Security",
            "finding": "Multi-factor authentication (MFA) is not enabled on the account.",
            "severity": "CRITICAL"
        })
        recommendations.append({
            "priority": "IMMEDIATE",
            "action": "Enable Multi-Factor Authentication (MFA) utilizing an authenticator app or hardware key."
        })
        
    if responses.get("unknown_connections") in ["YES", "OFTEN"]:
        findings.append({
            "category": "Social Engineering",
            "finding": "Connection requests from unknown individuals are routinely accepted.",
            "severity": "HIGH"
        })
        recommendations.append({
            "priority": "IMPORTANT",
            "action": "Implement a strict verification policy for connection requests; accept only known individuals."
        })
        
    return findings, recommendations
