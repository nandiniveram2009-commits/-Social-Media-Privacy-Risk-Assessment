# FILE NAME: improvement_simulator.py
# FILE PATH: backend/services/improvement_simulator.py
# PURPOSE: Simulates potential risk score reduction based on security remediations.

def simulate_improvements(current_score: float, selected_improvements: list) -> dict:
    reduction = 0.0
    impact_map = {
        "make_profile_private": 15.0,
        "hide_phone_number": 12.0,
        "disable_realtime_location": 15.0,
        "enable_mfa": 20.0,
        "enable_tag_review": 8.0,
        "revoke_unused_apps": 10.0,
        "restrict_unknown_connections": 10.0
    }
    
    for imp in selected_improvements:
        reduction += impact_map.get(imp, 5.0)
        
    simulated_score = max(0.0, round(current_score - reduction, 2))
    
    if simulated_score <= 20:
        simulated_level = "LOW"
    elif simulated_score <= 40:
        simulated_level = "MODERATE"
    elif simulated_score <= 70:
        simulated_level = "HIGH"
    else:
        simulated_level = "CRITICAL"
        
    return {
        "previous_score": current_score,
        "simulated_score": simulated_score,
        "risk_reduction_points": round(current_score - simulated_score, 2),
        "new_risk_level": simulated_level,
        "applied_improvements": selected_improvements
    }
