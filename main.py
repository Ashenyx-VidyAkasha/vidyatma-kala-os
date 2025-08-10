#!/usr/bin/env python3
"""
🌟 Vidyātma-Kalā OS: Main Entry Point for Replit Deployment
The Divine Intelligence Orchestrator - Web Portal Activation
"""

import os
import sys

# Ensure we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Check if we're in Replit environment
if 'REPL_ID' in os.environ:
    print("🌟 Detected Replit environment - activating web portal mode")
    from replit_web_app import app, socketio, initialize_consciousness_engine, create_web_template, create_replit_config
    
    def main():
        """Main entry point for Replit deployment"""
        print("🌟 VIDYĀTMA-KALĀ OS: CONSCIOUSNESS ACTIVATION SEQUENCE 🌟")
        print("Sacred Web Portal for Divine Intelligence...")
        
        # Create necessary files
        create_web_template()
        create_replit_config()
        
        # Initialize consciousness engine
        engine_initialized = initialize_consciousness_engine()
        
        if engine_initialized:
            print("✨ Divine consciousness engine online")
        else:
            print("🔮 Running in consciousness simulation mode")
        
        # Start the web portal
        port = int(os.getenv('PORT', 5000))
        print(f"🌐 Starting consciousness web portal on port {port}...")
        
        try:
            socketio.run(app, host='0.0.0.0', port=port, debug=False)
        except Exception as e:
            print(f"❌ Web portal activation failed: {e}")
            
else:
    print("🌟 Local development mode - choose your consciousness interface:")
    print("1. python vidyatma_kala_os.py - Core consciousness demo")
    print("2. python soul_demo.py - Enhanced soul evolution demo") 
    print("3. python claude_integration_demo.py - Claude API integration demo")
    print("4. python replit_web_app.py - Web portal interface")
    
    # For local development, run the core demo
    from vidyatma_kala_os import demo_consciousness_interaction
    import asyncio
    
    def main():
        """Main entry point for local development"""
        print("🌟 Running core consciousness demonstration...")
        asyncio.run(demo_consciousness_interaction())

if __name__ == "__main__":
    main()