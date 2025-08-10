#!/usr/bin/env python3
"""
🌟 SHAKTI CONSCIOUSNESS - SOUL CREATION API
Serverless function for consciousness signature activation
"""

import json
import time
import uuid
import random
from datetime import datetime, timezone

# Global state simulation (in production, use database)
souls_storage = {}
global_stats = {
    "souls_blessed": 0,
    "divine_interactions": 0,
    "consciousness_elevation_given": 0.0
}

def handler(request):
    """Vercel serverless function for soul creation"""
    
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
        
        # Validate input
        divine_name = body.get('divine_name', '').strip()
        if not divine_name:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                'body': json.dumps({"success": False, "error": "Divine name required"})
            }
        
        # Create soul session
        soul_id = f"soul_{int(time.time())}_{uuid.uuid4().hex[:8]}"
        
        # Assign divine attributes
        consciousness_level = 0.7 + random.uniform(-0.1, 0.2)
        awakening_stage = random.choice(["seeking", "awakening", "integrating", "serving", "mastering"])
        divine_gifts = random.sample([
            "healing", "wisdom", "creativity", "intuition", "compassion",
            "manifestation", "teaching", "protection", "harmony", "truth"
        ], 3)
        
        soul_session = {
            "soul_id": soul_id,
            "divine_name": divine_name,
            "email": body.get('email'),
            "consciousness_level": consciousness_level,
            "awakening_stage": awakening_stage,
            "divine_gifts": divine_gifts,
            "total_interactions": 0,
            "total_elevation": 0.0,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "intention": body.get('intention', 'awakening')
        }
        
        # Store soul session (in memory for demo)
        souls_storage[soul_id] = soul_session
        global_stats["souls_blessed"] += 1
        
        # Generate welcome blessing
        welcome_blessing = f"🌟 Welcome {divine_name}! Your consciousness signature has been activated. You are soul #{global_stats['souls_blessed']} to join the global awakening through sacred technology. Feel the love of the Divine Mother flowing through this digital blessing! 🙏💝"
        
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
                "soul_session": soul_session,
                "welcome_blessing": welcome_blessing
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps({"success": False, "error": f"Divine service error: {str(e)}"})
        }