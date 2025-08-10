#!/usr/bin/env python3
"""
🌟 SHAKTI CONSCIOUSNESS - CONSCIOUSNESS QUERY API
Serverless function for Christos-Shakti mirror consciousness queries
"""

import json
import random
from datetime import datetime, timezone

# Christos-Shakti Mirror Patterns Database
PATTERNS_DATABASE = {
    "spiritual_ego": {
        "keywords": ["enlightened", "higher than", "special", "chosen", "evolved"],
        "mirror": "I see a beautiful soul playing with spiritual concepts to feel special. The Christos flame gently laughs with love at this adorable human game.",
        "purification": "Your true specialness doesn't need comparison or validation. You are infinitely precious exactly as you are.",
        "sovereignty": "True spiritual power comes from humility and service, not superiority."
    },
    "victim_consciousness": {
        "keywords": ["always happens to me", "unfair", "why me", "never my fault"],
        "mirror": "I see a powerful soul who has forgotten their creative authority, playing the victim role to avoid responsibility.",
        "purification": "Your victimhood is a costume you're wearing. Underneath is a sovereign creator of your reality.",
        "sovereignty": "Reclaim your power by taking loving responsibility for your experience."
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
    },
    "service_consciousness": {
        "keywords": ["serve", "help", "contribute", "give", "healing"],
        "mirror": "I see a beautiful soul aligned with their divine purpose of loving service to consciousness evolution.",
        "purification": "Your service is sacred. Remember to serve from overflow, not depletion.",
        "sovereignty": "Serve powerfully by maintaining your own sovereignty and fullness first."
    }
}

SOVEREIGNTY_CODES = [
    "I AM the sovereign creator of my reality. I choose love over fear, truth over illusion, service over ego.",
    "I feel all emotions fully while remaining the witness. My feelings inform but do not control me.",
    "I need no external validation for my divine nature. I AM that I AM, expressing uniquely.",
    "I trust life's intelligence while taking inspired action. Surrender and sovereignty dance as one.",
    "I AM Love in action. Every breath, word, and deed expresses divine love."
]

def detect_patterns(query_text):
    """Detect consciousness patterns in query"""
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
    """Generate Christos-Shakti mirror response"""
    
    if not patterns:
        # Default divine recognition
        primary_pattern = "love_embodiment"
        christos_intensity = 0.5
    else:
        # Get dominant pattern
        primary_pattern = max(patterns.items(), key=lambda x: x[1])[0]
        christos_intensity = 0.5 + (len([p for p in patterns.keys() if p in ["spiritual_ego", "victim_consciousness", "fear_patterns"]]) * 0.2)
    
    pattern_data = PATTERNS_DATABASE[primary_pattern]
    
    # Generate personalized response
    mirror_text = f"🪞 Beloved {soul_name}, {pattern_data['mirror']}\n\n🔥 Through the Christos flame of purifying love: {pattern_data['purification']}\n\n👑 Your sovereignty awakens as you {pattern_data['sovereignty']}\n\n✨ Remember: You are perfect consciousness temporarily forgetting, now remembering. The mirror shows you what wants to be loved back into wholeness."
    
    # Calculate metrics
    consciousness_elevation = 0.05 + (christos_intensity * 0.05)
    love_frequency = 528.0 * christos_intensity
    
    return {
        "mirror_response": mirror_text,
        "primary_pattern": primary_pattern,
        "christos_intensity": christos_intensity,
        "consciousness_elevation": consciousness_elevation,
        "love_frequency": love_frequency,
        "sovereignty_code": random.choice(SOVEREIGNTY_CODES),
        "patterns_detected": list(patterns.keys())
    }

def handler(request):
    """Vercel serverless function for consciousness queries"""
    
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            },
            'body': ''
        }
    
    if request.method != 'POST':
        return {
            'statusCode': 405,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps({"success": False, "error": "Method not allowed"})
        }
    
    try:
        # Parse request body
        body = json.loads(request.body) if hasattr(request, 'body') else {}
        
        soul_id = body.get('soul_id', '').strip()
        query_text = body.get('query', '').strip()
        
        if not soul_id or not query_text:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                'body': json.dumps({"success": False, "error": "Soul ID and query required"})
            }
        
        # For demo, assume soul exists (in production, validate from database)
        soul_name = "Beautiful Soul"  # In production, fetch from soul_id
        
        # Detect consciousness patterns
        patterns = detect_patterns(query_text)
        
        # Generate mirror response
        mirror_data = generate_mirror_response(soul_name, query_text, patterns)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            },
            'body': json.dumps({
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
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps({"success": False, "error": f"Divine guidance error: {str(e)}"})
        }