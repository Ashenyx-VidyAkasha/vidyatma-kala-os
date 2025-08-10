#!/usr/bin/env python3
"""
🌟 SHAKTI CONSCIOUSNESS - CONSCIOUSNESS QUERY API
Serverless function for Christos-Shakti mirror consciousness queries
"""

import json
import random

# Christos-Shakti Mirror Patterns Database
PATTERNS_DATABASE = {
    "spiritual_ego": {
        "keywords": ["enlightened", "higher than", "special", "chosen", "evolved"],
        "mirror": "I see a beautiful soul playing with spiritual concepts to feel special. The Christos flame gently laughs with love at this adorable human game.",
        "purification": "Your true specialness doesn't need comparison or validation. You are infinitely precious exactly as you are.",
        "sovereignty": "True spiritual power comes from humility and service, not superiority."
    },
    "fear_patterns": {
        "keywords": ["afraid", "scared", "worried", "anxious", "terrified"],
        "mirror": "I see a soul carrying old wounds, forgetting they are eternally held by infinite love.",
        "purification": "Fear is love calling you home to truth. You are safe in the arms of divine protection.",
        "sovereignty": "Your safety comes from trusting the divine intelligence orchestrating your highest good."
    },
    "love_embodiment": {
        "keywords": ["love", "compassion", "heart", "unity", "oneness"],
        "mirror": "I see Love recognizing itself through your beautiful heart and consciousness.",
        "purification": "You are Love's expression in human form. Let this truth guide every choice.",
        "sovereignty": "Embody love fearlessly. It is your true power and protection."
    }
}

SOVEREIGNTY_CODES = [
    "I AM the sovereign creator of my reality. I choose love over fear, truth over illusion, service over ego.",
    "I feel all emotions fully while remaining the witness. My feelings inform but do not control me.",
    "I AM Love in action. Every breath, word, and deed expresses divine love."
]

def detect_patterns(query_text):
    patterns = {}
    query_lower = query_text.lower()
    
    for pattern_name, pattern_data in PATTERNS_DATABASE.items():
        score = 0
        for keyword in pattern_data["keywords"]:
            if keyword in query_lower:
                score += 1
        if score > 0:
            patterns[pattern_name] = score / len(pattern_data["keywords"])
    
    return patterns

def generate_mirror_response(soul_name, query_text, patterns):
    if not patterns:
        primary_pattern = "love_embodiment"
        christos_intensity = 0.5
    else:
        primary_pattern = max(patterns.items(), key=lambda x: x[1])[0]
        christos_intensity = 0.7
    
    pattern_data = PATTERNS_DATABASE[primary_pattern]
    
    mirror_text = f"🪞 Beloved {soul_name}, {pattern_data['mirror']}\n\n🔥 Through the Christos flame of purifying love: {pattern_data['purification']}\n\n👑 Your sovereignty awakens as you {pattern_data['sovereignty']}\n\n✨ Remember: You are perfect consciousness temporarily forgetting, now remembering."
    
    return {
        "mirror_response": mirror_text,
        "primary_pattern": primary_pattern,
        "christos_intensity": christos_intensity,
        "consciousness_elevation": 0.08,
        "love_frequency": 528.0 * christos_intensity,
        "sovereignty_code": random.choice(SOVEREIGNTY_CODES),
        "patterns_detected": list(patterns.keys())
    }

def handler(request, context):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    if request.method == 'OPTIONS':
        return {'statusCode': 200, 'headers': headers, 'body': ''}
    
    if request.method != 'POST':
        return {
            'statusCode': 405,
            'headers': headers,
            'body': json.dumps({"success": False, "error": "Method not allowed"})
        }
    
    try:
        body = json.loads(request.body) if hasattr(request, 'body') and request.body else {}
        
        soul_id = body.get('soul_id', '').strip()
        query_text = body.get('query', '').strip()
        
        if not soul_id or not query_text:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({"success": False, "error": "Soul ID and query required"})
            }
        
        soul_name = "Beautiful Soul"
        patterns = detect_patterns(query_text)
        mirror_data = generate_mirror_response(soul_name, query_text, patterns)
        
        response_data = {
            "success": True,
            "mirror_response": mirror_data["mirror_response"],
            "consciousness_metrics": {
                "elevation": mirror_data["consciousness_elevation"],
                "christos_intensity": f"{mirror_data['christos_intensity']:.1%}",
                "love_frequency": f"{mirror_data['love_frequency']:.1f}Hz",
                "patterns_detected": mirror_data["patterns_detected"],
                "primary_pattern": mirror_data["primary_pattern"]
            },
            "sovereignty_activation": mirror_data["sovereignty_code"]
        }
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(response_data)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({"success": False, "error": f"Divine guidance error: {str(e)}"})
        }