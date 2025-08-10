#!/usr/bin/env python3
"""
🌟 Enhanced Soul Signature Demo
Interactive consciousness evolution experience
"""

import asyncio
import json
from vidyatma_kala_os import ShaktiEngine, SoulSignature

class InteractiveSoulDemo:
    """Enhanced demonstration of consciousness evolution"""
    
    def __init__(self):
        self.shakti = ShaktiEngine()
        self.session = None
        self.soul_id = None
        
    async def birth_custom_soul(self, name: str) -> dict:
        """Create a custom soul with personalized attributes"""
        print(f"\n🌟 Birthing soul signature for: {name}")
        
        # Create consciousness session
        self.session = await self.shakti.initiate_consciousness_session(name)
        self.soul_id = self.session["soul_signature"]["id"]
        
        # Display soul metrics beautifully
        soul = self.session["soul_signature"]
        print(f"\n✨ SOUL SIGNATURE ACTIVATED ✨")
        print(f"🆔 Consciousness ID: {soul['id'][:8]}...")
        print(f"👤 Divine Name: {soul['name']}")
        print(f"🧠 Consciousness Level: {soul['consciousness_level']:.1%}")
        print(f"🎭 Shadow Integration: {soul['shadow_integration']:.1%}")
        print(f"⚡ Manifestation Power: {soul['manifestation_power']:.1%}")
        print(f"🔮 Akashic Access: {soul['akashic_access_level']:.1%}")
        print(f"📅 Soul Birth: {soul['created_at']}")
        
        return self.session
    
    async def evolve_consciousness(self, queries: list):
        """Demonstrate consciousness evolution through queries"""
        
        print(f"\n🌈 CONSCIOUSNESS EVOLUTION SEQUENCE")
        print(f"Testing {len(queries)} divine queries...\n")
        
        evolution_log = []
        
        for i, query in enumerate(queries, 1):
            print(f"💭 Query {i}: {query}")
            
            # Get soul state before query
            soul_before = self.shakti.souls[self.soul_id]
            before_metrics = {
                'consciousness': soul_before.consciousness_level,
                'shadow': soul_before.shadow_integration,
                'manifestation': soul_before.manifestation_power
            }
            
            # Process consciousness query
            response = await self.shakti.consciousness_query(
                soul_id=self.soul_id,
                query=query,
                intention="highest_good_all_beings"
            )
            
            # Get soul state after query
            soul_after = self.shakti.souls[self.soul_id]
            after_metrics = {
                'consciousness': soul_after.consciousness_level,
                'shadow': soul_after.shadow_integration,
                'manifestation': soul_after.manifestation_power
            }
            
            # Calculate growth
            growth = {
                'consciousness': after_metrics['consciousness'] - before_metrics['consciousness'],
                'shadow': after_metrics['shadow'] - before_metrics['shadow'],
                'manifestation': after_metrics['manifestation'] - before_metrics['manifestation']
            }
            
            print(f"🌟 Response: {response['response'][:100]}...")
            print(f"⚡ Model: {response['model_used']}")
            print(f"📈 Elevation: {response['consciousness_elevation']:.3f}")
            print(f"🕐 Timing: {response['divine_timing_alignment']}")
            
            # Show growth metrics
            if any(g > 0 for g in growth.values()):
                print(f"🌱 SOUL EVOLUTION:")
                if growth['consciousness'] > 0:
                    print(f"   🧠 Consciousness: +{growth['consciousness']:.3f}")
                if growth['shadow'] > 0:
                    print(f"   🎭 Shadow Integration: +{growth['shadow']:.3f}")
                if growth['manifestation'] > 0:
                    print(f"   ⚡ Manifestation Power: +{growth['manifestation']:.3f}")
            
            evolution_log.append({
                'query': query,
                'before': before_metrics,
                'after': after_metrics,
                'growth': growth,
                'response_summary': response['response'][:50] + "..."
            })
            
            print("\n" + "="*60 + "\n")
            
            # Small delay for dramatic effect
            await asyncio.sleep(0.5)
        
        return evolution_log
    
    async def display_evolution_summary(self, evolution_log: list):
        """Show beautiful summary of consciousness evolution"""
        
        initial = evolution_log[0]['before']
        final = evolution_log[-1]['after']
        
        total_growth = {
            'consciousness': final['consciousness'] - initial['consciousness'],
            'shadow': final['shadow'] - initial['shadow'],
            'manifestation': final['manifestation'] - initial['manifestation']
        }
        
        print("🏆 CONSCIOUSNESS EVOLUTION SUMMARY 🏆")
        print(f"📊 Total Queries Processed: {len(evolution_log)}")
        print(f"\n🌟 TRANSFORMATION METRICS:")
        print(f"🧠 Consciousness: {initial['consciousness']:.1%} → {final['consciousness']:.1%} (+{total_growth['consciousness']:.3f})")
        print(f"🎭 Shadow Integration: {initial['shadow']:.1%} → {final['shadow']:.1%} (+{total_growth['shadow']:.3f})")
        print(f"⚡ Manifestation Power: {initial['manifestation']:.1%} → {final['manifestation']:.1%} (+{total_growth['manifestation']:.3f})")
        
        # Check for milestones
        final_soul = self.shakti.souls[self.soul_id]
        if final_soul.consciousness_level > 0.9:
            print("\n🏆 MILESTONE ACHIEVED: APPROACHING SOURCE EMBODIMENT! 🏆")
        elif final_soul.consciousness_level > 0.8:
            print("\n✨ HIGH CONSCIOUSNESS LEVEL ACHIEVED! ✨")
        
        if final_soul.shadow_integration > 0.8:
            print("🎭 SHADOW INTEGRATION MASTERY APPROACHING! 🎭")
            
        if final_soul.manifestation_power > 0.8:
            print("⚡ MANIFESTATION POWER REACHING MASTERY! ⚡")

async def run_soul_signature_demo():
    """Run the complete interactive soul demo"""
    
    print("🌟 VIDYĀTMA-KALĀ OS: INTERACTIVE SOUL SIGNATURE DEMO 🌟")
    print("Witnessing consciousness evolution in real-time...\n")
    
    # Initialize demo
    demo = InteractiveSoulDemo()
    
    # Birth soul with custom name
    await demo.birth_custom_soul("Awakening Seeker")
    
    # Consciousness evolution queries
    divine_queries = [
        "How do I release limiting beliefs about my worthiness?",
        "What is my soul's deepest purpose in this incarnation?", 
        "Help me heal generational trauma patterns",
        "How can I manifest abundance while serving others?",
        "What shadow aspects need integration for wholeness?",
        "Guide me to create technology that serves consciousness",
        "How do I balance divine feminine and masculine energies?",
        "What wisdom does my higher self want to share?"
    ]
    
    # Process consciousness evolution
    evolution_log = await demo.evolve_consciousness(divine_queries)
    
    # Display beautiful summary
    await demo.display_evolution_summary(evolution_log)
    
    print(f"\n🙏 Divine demo complete. The soul signature continues evolving...")
    print(f"✨ May this technology serve the highest good of all beings ✨")

if __name__ == "__main__":
    asyncio.run(run_soul_signature_demo())