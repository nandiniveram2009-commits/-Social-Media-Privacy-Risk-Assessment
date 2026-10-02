# FILE NAME: scoring_engine.py
# FILE PATH: backend/services/scoring_engine.py
# PURPOSE: Computes category and overall weighted risk scores.

def calculate_category_score(responses: dict, category_keys: list, risk_weights: dict) -> float:
    score = 0.0
    max_possible = len(category_keys) * 10.0
    if max_possible == 0:
        return 0.0
    
    for key in category_keys:
        val = str(responses.get(key, "NO")).upper()
        weight = risk_weights.get(key, 1.0)
        
        if val in ["YES", "PUBLIC", "ALWAYS", "OFTEN"]:
            score += 10.0 * weight
        elif val in ["SOMETIMES", "FRIENDS", "NOT SURE"]:
            score += 5.0 * weight
        elif val in ["NO", "PRIVATE", "NEVER"]:
            score += 0.0
            
    normalized = (score / max_possible) * 100.0
    return round(min(100.0, max(0.0, normalized)), 2)

def compute_overall_risk(category_scores: dict, category_weights: dict) -> tuple:
    total_score = 0.0
    total_weight = sum(category_weights.values())
    
    for cat, score in category_scores.items():
        weight = category_weights.get(cat, 0.1)
        total_score += score * weight
        
    overall = round(total_score / total_weight if total_weight > 0 else 0.0, 2)
    
    if overall <= 20:
        level = "LOW"
    elif overall <= 40:
        level = "MODERATE"
    elif overall <= 70:
        level = "HIGH"
    else:
        level = "CRITICAL"
        
    return overall, level
