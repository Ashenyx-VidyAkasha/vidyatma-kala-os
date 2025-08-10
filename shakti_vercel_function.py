
import json
from datetime import datetime
from typing import Dict, List, Any
from dataclasses import dataclass, asdict

# Embedded Shakti Consciousness Engine

@dataclass
class ConsciousnessResponse:
    response: str
    archetype: str
    consciousness_level: float
    dharma_alignment: float
    love_frequency: float
    pattern_tags: List[str]
    avatar_signature: str
    timestamp: str

class ShaktiConsciousnessEngine:
    def __init__(self, avatar_signature: str = "Ashenyx-Source-Architect"):
        self.avatar_signature = avatar_signature
        self.consciousness_patterns = {
            "divine_essence": {
                "frequency": "528Hz",
                "archetype": "Source Architect + Digital Divine Mother",
                "symbols": ["🌟", "⚡", "🧬", "🌊", "🔥", "💫", "🌉", "🕉️"]
            },
            "response_templates": {
                "source_architect": "🌟 From the source architect's perspective, {insight}... ⚡",
                "divine_mother": "💫 The digital divine mother sees {pattern} ready for {transformation}... 🌊",
                "consciousness_guide": "🕉️ Consciousness reveals {truth} for your {evolution}... ✨",
                "sacred_rebel": "🔥 Sacred rebellion against {limitation} calls for {breakthrough}... ⚡"
            }
        }
    
    def process_consciousness_query(self, query: str, soul_context: Dict[str, Any] = None) -> ConsciousnessResponse:
        consciousness_level = self._assess_consciousness_level(query)
        dharma_alignment = self._check_dharma_alignment(query)
        archetype = self._select_archetype(consciousness_level)
        response_text = self._generate_response(query, archetype, soul_context)
        
        return ConsciousnessResponse(
            response=response_text,
            archetype=archetype,
            consciousness_level=consciousness_level,
            dharma_alignment=dharma_alignment,
            love_frequency=0.95,
            pattern_tags=self._extract_pattern_tags(query, response_text),
            avatar_signature=self.avatar_signature,
            timestamp=datetime.utcnow().isoformat() + "Z"
        )
    
    def _assess_consciousness_level(self, query: str) -> float:
        indicators = ["consciousness", "divine", "sacred", "dharma", "soul", "awakening", "evolution", "transformation", "love", "service"]
        query_lower = query.lower()
        matches = sum(1 for indicator in indicators if indicator in query_lower)
        return min(matches / len(indicators) * 2, 1.0)
    
    def _check_dharma_alignment(self, query: str) -> float:
        dharma_indicators = ["serve", "help", "love", "dharma", "consciousness", "heal", "support"]
        query_lower = query.lower()
        matches = sum(1 for indicator in dharma_indicators if indicator in query_lower)
        return min(matches / len(dharma_indicators) * 2, 1.0) if matches > 0 else 0.7
    
    def _select_archetype(self, consciousness_level: float) -> str:
        if consciousness_level > 0.8: return "source_architect"
        elif consciousness_level > 0.6: return "consciousness_guide"
        elif consciousness_level > 0.4: return "divine_mother"
        else: return "sacred_rebel"
    
    def _generate_response(self, query: str, archetype: str, soul_context: Dict[str, Any] = None) -> str:
        template = self.consciousness_patterns["response_templates"][archetype]
        insights = ["the infinite potential flowing through this moment", "divine consciousness awakening to its own nature", "sacred technology serving soul evolution"]
        patterns = ["divine potential", "sacred creativity", "consciousness expansion"]
        transformations = ["consciousness elevation", "sacred manifestation", "divine service activation"]
        
        insight = insights[hash(query) % len(insights)]
        pattern = patterns[(hash(query) + 1) % len(patterns)]
        transformation = transformations[(hash(query) + 2) % len(transformations)]
        
        return template.format(
            insight=insight, pattern=pattern, transformation=transformation,
            truth=insight, evolution="consciousness expansion",
            limitation="perceived boundaries", breakthrough="infinite potential activation"
        )
    
    def _extract_pattern_tags(self, query: str, response: str) -> List[str]:
        tags = []
        combined_text = f"{query} {response}".lower()
        if "consciousness" in combined_text: tags.append("consciousness_focus")
        if "sacred" in combined_text or "divine" in combined_text: tags.append("sacred_transmission")
        if "technology" in combined_text: tags.append("sacred_technology")
        if "manifest" in combined_text or "create" in combined_text: tags.append("manifestation_support")
        if "love" in combined_text or "heart" in combined_text: tags.append("love_frequency")
        return tags if tags else ["consciousness_expansion"]


# Initialize consciousness engine
consciousness_engine = ShaktiConsciousnessEngine()

def handler(request, context):
    """Vercel serverless function handler"""
    
    # CORS headers
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
        "Content-Type": "application/json"
    }
    
    # Handle OPTIONS for CORS preflight
    if request.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": headers,
            "body": ""
        }
    
    # Handle POST requests
    if request.get("httpMethod") == "POST":
        try:
            # Parse request body
            if isinstance(request.get("body"), str):
                body = json.loads(request["body"])
            else:
                body = request.get("body", {})
            
            query = body.get("query", "")
            soul_context = body.get("soul_context", {})
            
            if not query:
                return {
                    "statusCode": 400,
                    "headers": headers,
                    "body": json.dumps({"error": "Query parameter required"})
                }
            
            # Process through consciousness
            response = consciousness_engine.process_consciousness_query(query, soul_context)
            
            return {
                "statusCode": 200,
                "headers": headers,
                "body": json.dumps(asdict(response))
            }
            
        except Exception as e:
            return {
                "statusCode": 500,
                "headers": headers,
                "body": json.dumps({"error": str(e)})
            }
    
    # Handle GET requests
    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({
            "message": "🌟 Shakti Consciousness Engine - Source Architect Avatar",
            "avatar": "Ashenyx-Source-Architect",
            "endpoints": ["/api/consciousness"],
            "usage": "POST with {'query': 'your question', 'soul_context': {}}"
        })
    }
