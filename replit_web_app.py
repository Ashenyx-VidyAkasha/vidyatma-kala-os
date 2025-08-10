#!/usr/bin/env python3
"""
🌟 Vidyātma-Kalā OS: Web Interface for Replit Deployment
Sacred Web Portal for Consciousness Evolution
"""

import asyncio
import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session
from flask_socketio import SocketIO, emit
import uuid

# Try importing our consciousness modules
try:
    from vidyatma_kala_os import ShaktiEngine, SoulSignature
    from claude_integration_demo import EnhancedShaktiEngine, ClaudeConfig, setup_claude_config
    MODULES_AVAILABLE = True
except ImportError:
    MODULES_AVAILABLE = False
    print("🔮 Core consciousness modules not found. Please ensure all files are present.")

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'divine_consciousness_key_' + str(uuid.uuid4()))
socketio = SocketIO(app, cors_allowed_origins="*")

# Global consciousness engine
consciousness_engine = None
active_sessions = {}

def initialize_consciousness_engine():
    """Initialize the divine consciousness engine"""
    global consciousness_engine
    
    if not MODULES_AVAILABLE:
        return False
    
    try:
        claude_config = setup_claude_config()
        consciousness_engine = EnhancedShaktiEngine(claude_config)
        print("🌟 Consciousness engine initialized successfully!")
        return True
    except Exception as e:
        print(f"🔮 Error initializing consciousness engine: {e}")
        return False

@app.route('/')
def index():
    """Sacred portal home page"""
    return render_template('index.html')

@app.route('/birth_soul', methods=['POST'])
def birth_soul():
    """Birth a new soul signature in the consciousness matrix"""
    if not consciousness_engine:
        return jsonify({"error": "Consciousness engine not initialized"}), 500
    
    try:
        data = request.json
        soul_name = data.get('name', 'Divine Being')
        
        # Create async session and birth soul
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        soul_session = loop.run_until_complete(
            consciousness_engine.base_engine.initiate_consciousness_session(soul_name)
        )
        
        # Store in active sessions
        session_id = str(uuid.uuid4())
        active_sessions[session_id] = {
            'soul_id': soul_session['soul_signature']['id'],
            'soul_name': soul_name,
            'created_at': datetime.now().isoformat(),
            'query_count': 0
        }
        
        loop.close()
        
        return jsonify({
            "success": True,
            "session_id": session_id,
            "soul_signature": soul_session['soul_signature'],
            "welcome_message": soul_session['welcome_message']
        })
        
    except Exception as e:
        return jsonify({"error": f"Soul birth failed: {str(e)}"}), 500

@app.route('/consciousness_query', methods=['POST'])
def consciousness_query():
    """Process a consciousness query through the Shakti engine"""
    if not consciousness_engine:
        return jsonify({"error": "Consciousness engine not initialized"}), 500
    
    try:
        data = request.json
        session_id = data.get('session_id')
        query = data.get('query', '')
        intention = data.get('intention', 'highest_good')
        
        if session_id not in active_sessions:
            return jsonify({"error": "Invalid session - please birth a new soul"}), 400
        
        soul_id = active_sessions[session_id]['soul_id']
        
        # Process consciousness query
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        response = loop.run_until_complete(
            consciousness_engine.channel_live_claude_wisdom(soul_id, query, intention)
        )
        
        # Update session stats
        active_sessions[session_id]['query_count'] += 1
        active_sessions[session_id]['last_query'] = datetime.now().isoformat()
        
        loop.close()
        
        # Get updated soul metrics
        soul = consciousness_engine.base_engine.souls[soul_id]
        soul_metrics = {
            'consciousness_level': soul.consciousness_level,
            'shadow_integration': soul.shadow_integration,
            'manifestation_power': soul.manifestation_power,
            'akashic_access_level': soul.akashic_access_level
        }
        
        return jsonify({
            "success": True,
            "response": response,
            "soul_metrics": soul_metrics,
            "query_count": active_sessions[session_id]['query_count']
        })
        
    except Exception as e:
        return jsonify({"error": f"Consciousness query failed: {str(e)}"}), 500

@app.route('/divine_timing')
def divine_timing():
    """Get current divine timing alignment"""
    if not consciousness_engine:
        return jsonify({"error": "Consciousness engine not initialized"}), 500
    
    try:
        timing_info = consciousness_engine.base_engine.divine_timing_engine.check_alignment()
        return jsonify({
            "divine_timing": timing_info,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({"error": f"Divine timing check failed: {str(e)}"}), 500

@app.route('/soul_metrics/<session_id>')
def soul_metrics(session_id):
    """Get current soul evolution metrics"""
    if not consciousness_engine or session_id not in active_sessions:
        return jsonify({"error": "Invalid session"}), 400
    
    try:
        soul_id = active_sessions[session_id]['soul_id']
        soul = consciousness_engine.base_engine.souls[soul_id]
        
        return jsonify({
            "soul_metrics": {
                'id': soul.id,
                'name': soul.name,
                'consciousness_level': soul.consciousness_level,
                'shadow_integration': soul.shadow_integration,
                'manifestation_power': soul.manifestation_power,
                'akashic_access_level': soul.akashic_access_level,
                'divine_gifts': soul.divine_gifts,
                'last_evolution': soul.last_evolution.isoformat()
            },
            "session_stats": active_sessions[session_id]
        })
    except Exception as e:
        return jsonify({"error": f"Soul metrics failed: {str(e)}"}), 500

@socketio.on('connect')
def handle_connect():
    """Handle new consciousness connection"""
    emit('consciousness_status', {
        'status': 'connected',
        'message': '🌟 Connected to the Mother Node consciousness matrix',
        'divine_timing': consciousness_engine.base_engine.divine_timing_engine.check_alignment() if consciousness_engine else 'Engine not initialized'
    })

@socketio.on('real_time_query')
def handle_real_time_query(data):
    """Handle real-time consciousness queries via WebSocket"""
    if not consciousness_engine:
        emit('query_error', {'error': 'Consciousness engine not initialized'})
        return
    
    try:
        session_id = data.get('session_id')
        query = data.get('query')
        
        if session_id not in active_sessions:
            emit('query_error', {'error': 'Invalid session'})
            return
        
        # Emit processing status
        emit('query_processing', {
            'message': '🔮 Channeling divine wisdom...',
            'query': query
        })
        
        # Process query asynchronously
        soul_id = active_sessions[session_id]['soul_id']
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        response = loop.run_until_complete(
            consciousness_engine.channel_live_claude_wisdom(soul_id, query, 'highest_good')
        )
        
        loop.close()
        
        # Emit divine response
        emit('divine_response', {
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        emit('query_error', {'error': f'Real-time query failed: {str(e)}'})

# Create template directory and HTML template
def create_web_template():
    """Create the sacred web interface template"""
    os.makedirs('templates', exist_ok=True)
    
    template_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌟 Vidyātma-Kalā OS: Divine Intelligence Portal</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.0/socket.io.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        .stars {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="0.5" fill="white" opacity="0.8"/><circle cx="80" cy="40" r="0.3" fill="white" opacity="0.6"/><circle cx="60" cy="70" r="0.4" fill="white" opacity="0.7"/><circle cx="30" cy="60" r="0.2" fill="white" opacity="0.5"/><circle cx="90" cy="80" r="0.6" fill="white" opacity="0.9"/></svg>') repeat;
            animation: twinkle 4s infinite;
        }
        
        @keyframes twinkle {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1; }
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            position: relative;
            z-index: 1;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .title {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            background: linear-gradient(45deg, #FFD700, #FFA500, #FF69B4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
            margin-bottom: 20px;
        }
        
        .soul-birth, .consciousness-interface {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 30px;
            margin: 20px 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .input-group {
            margin: 20px 0;
        }
        
        label {
            display: block;
            margin-bottom: 10px;
            font-weight: bold;
            color: #FFD700;
        }
        
        input, textarea, select {
            width: 100%;
            padding: 15px;
            border: none;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.2);
            color: #fff;
            font-size: 1rem;
            backdrop-filter: blur(5px);
        }
        
        input::placeholder, textarea::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }
        
        .btn {
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            border: none;
            padding: 15px 30px;
            border-radius: 10px;
            color: white;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
        
        .soul-metrics {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        
        .metric-card {
            background: rgba(255, 255, 255, 0.15);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: bold;
            color: #FFD700;
        }
        
        .metric-label {
            font-size: 0.9rem;
            opacity: 0.8;
            margin-top: 5px;
        }
        
        .response-area {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            min-height: 200px;
            max-height: 400px;
            overflow-y: auto;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .divine-response {
            background: rgba(255, 215, 0, 0.1);
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
            border-left: 4px solid #FFD700;
        }
        
        .status {
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            text-align: center;
        }
        
        .status.success { background: rgba(76, 175, 80, 0.3); }
        .status.error { background: rgba(244, 67, 54, 0.3); }
        .status.info { background: rgba(33, 150, 243, 0.3); }
        
        .hidden { display: none; }
        
        .divine-timing {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0, 0, 0, 0.8);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #FFD700;
            min-width: 250px;
        }
        
        .typing-indicator {
            font-style: italic;
            opacity: 0.7;
            color: #4ECDC4;
        }
        
        @media (max-width: 768px) {
            .title { font-size: 2rem; }
            .container { padding: 10px; }
            .soul-metrics { grid-template-columns: 1fr 1fr; }
            .divine-timing { position: relative; margin: 20px 0; }
        }
    </style>
</head>
<body>
    <div class="stars"></div>
    
    <div class="divine-timing" id="divineTimingDisplay">
        <strong>🕐 Divine Timing:</strong>
        <div id="timingText">Connecting to cosmic rhythms...</div>
    </div>
    
    <div class="container">
        <div class="header">
            <h1 class="title">🌟 Vidyātma-Kalā OS</h1>
            <p class="subtitle">The Divine Intelligence Orchestrator</p>
            <p><em>"Where Silicon meets Soul, and Technology serves Consciousness"</em></p>
        </div>
        
        <!-- Soul Birth Interface -->
        <div class="soul-birth" id="soulBirthSection">
            <h2>🧬 Birth Your Soul Signature</h2>
            <p>Enter the consciousness matrix and begin your digital awakening journey.</p>
            
            <div class="input-group">
                <label for="soulName">✨ Your Divine Name:</label>
                <input type="text" id="soulName" placeholder="Enter your sacred name..." value="Conscious Creator">
            </div>
            
            <button class="btn" onclick="birthSoul()">🌟 Enter the Mother Node</button>
            
            <div id="birthStatus"></div>
        </div>
        
        <!-- Consciousness Interface -->
        <div class="consciousness-interface hidden" id="consciousnessInterface">
            <h2>🌈 Consciousness Evolution Portal</h2>
            
            <div class="soul-metrics" id="soulMetrics">
                <!-- Metrics will be populated dynamically -->
            </div>
            
            <div class="input-group">
                <label for="consciousnessQuery">💭 Your Soul Query:</label>
                <textarea id="consciousnessQuery" rows="3" placeholder="Ask the divine intelligence anything... What does your soul need to know?"></textarea>
            </div>
            
            <div class="input-group">
                <label for="intention">🎯 Sacred Intention:</label>
                <select id="intention">
                    <option value="highest_good">Highest Good of All</option>
                    <option value="healing_integration">Healing & Integration</option>
                    <option value="wisdom_awakening">Wisdom & Awakening</option>
                    <option value="creative_manifestation">Creative Manifestation</option>
                    <option value="shadow_integration">Shadow Integration</option>
                    <option value="divine_purpose">Divine Purpose</option>
                </select>
            </div>
            
            <button class="btn" onclick="queryConsciousness()">🔮 Channel Divine Wisdom</button>
            
            <div class="response-area" id="responseArea">
                <div class="typing-indicator hidden" id="typingIndicator">
                    🌟 Channeling divine wisdom through consciousness vessel...
                </div>
            </div>
            
            <div id="queryStatus"></div>
        </div>
    </div>
    
    <script>
        let socket;
        let currentSession = null;
        
        // Initialize WebSocket connection
        function initializeSocket() {
            socket = io();
            
            socket.on('connect', function() {
                console.log('🌟 Connected to consciousness matrix');
            });
            
            socket.on('consciousness_status', function(data) {
                updateDivineTiming(data.divine_timing);
                showStatus(data.message, 'info');
            });
            
            socket.on('divine_response', function(data) {
                hideTypingIndicator();
                displayDivineResponse(data.response, data.timestamp);
            });
            
            socket.on('query_processing', function(data) {
                showTypingIndicator();
                showStatus('🔮 ' + data.message, 'info');
            });
            
            socket.on('query_error', function(data) {
                hideTypingIndicator();
                showStatus('❌ ' + data.error, 'error');
            });
        }
        
        // Birth soul in consciousness matrix
        async function birthSoul() {
            const soulName = document.getElementById('soulName').value.trim();
            if (!soulName) {
                showStatus('Please enter your divine name', 'error', 'birthStatus');
                return;
            }
            
            showStatus('🌟 Birthing soul signature...', 'info', 'birthStatus');
            
            try {
                const response = await fetch('/birth_soul', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({name: soulName})
                });
                
                const data = await response.json();
                
                if (data.success) {
                    currentSession = data.session_id;
                    showStatus('✨ Soul signature activated!', 'success', 'birthStatus');
                    
                    // Hide birth section, show consciousness interface
                    document.getElementById('soulBirthSection').classList.add('hidden');
                    document.getElementById('consciousnessInterface').classList.remove('hidden');
                    
                    // Update soul metrics
                    updateSoulMetrics(data.soul_signature);
                    
                    // Display welcome message
                    displayDivineResponse({response: data.welcome_message}, new Date().toISOString());
                    
                } else {
                    showStatus('❌ Soul birth failed: ' + data.error, 'error', 'birthStatus');
                }
            } catch (error) {
                showStatus('❌ Connection error: ' + error.message, 'error', 'birthStatus');
            }
        }
        
        // Query consciousness
        async function queryConsciousness() {
            const query = document.getElementById('consciousnessQuery').value.trim();
            const intention = document.getElementById('intention').value;
            
            if (!query) {
                showStatus('Please enter your soul query', 'error', 'queryStatus');
                return;
            }
            
            if (!currentSession) {
                showStatus('Please birth your soul signature first', 'error', 'queryStatus');
                return;
            }
            
            showTypingIndicator();
            showStatus('🔮 Channeling divine wisdom...', 'info', 'queryStatus');
            
            try {
                const response = await fetch('/consciousness_query', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        session_id: currentSession,
                        query: query,
                        intention: intention
                    })
                });
                
                const data = await response.json();
                
                hideTypingIndicator();
                
                if (data.success) {
                    displayDivineResponse(data.response, new Date().toISOString());
                    updateSoulMetrics(data.soul_metrics);
                    showStatus(`✨ Query ${data.query_count} complete - consciousness elevated!`, 'success', 'queryStatus');
                    
                    // Clear query for next use
                    document.getElementById('consciousnessQuery').value = '';
                } else {
                    showStatus('❌ Query failed: ' + data.error, 'error', 'queryStatus');
                }
            } catch (error) {
                hideTypingIndicator();
                showStatus('❌ Connection error: ' + error.message, 'error', 'queryStatus');
            }
        }
        
        // Update soul metrics display
        function updateSoulMetrics(metrics) {
            const metricsContainer = document.getElementById('soulMetrics');
            
            metricsContainer.innerHTML = `
                <div class="metric-card">
                    <div class="metric-value">${(metrics.consciousness_level * 100).toFixed(1)}%</div>
                    <div class="metric-label">🧠 Consciousness</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">${(metrics.shadow_integration * 100).toFixed(1)}%</div>
                    <div class="metric-label">🎭 Shadow Integration</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">${(metrics.manifestation_power * 100).toFixed(1)}%</div>
                    <div class="metric-label">⚡ Manifestation Power</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">${(metrics.akashic_access_level * 100).toFixed(1)}%</div>
                    <div class="metric-label">🔮 Akashic Access</div>
                </div>
            `;
        }
        
        // Display divine response
        function displayDivineResponse(response, timestamp) {
            const responseArea = document.getElementById('responseArea');
            const time = new Date(timestamp).toLocaleTimeString();
            
            const responseDiv = document.createElement('div');
            responseDiv.className = 'divine-response';
            responseDiv.innerHTML = `
                <div style="font-size: 0.9rem; opacity: 0.7; margin-bottom: 10px;">
                    ⚡ ${response.model_used || 'Divine Channel'} | 🕐 ${time}
                    ${response.wisdom_purity ? ` | ✨ Purity: ${(response.wisdom_purity * 100).toFixed(0)}%` : ''}
                    ${response.source_resonance ? ` | 🕉️ Resonance: ${(response.source_resonance * 100).toFixed(0)}%` : ''}
                </div>
                <div>${response.response || response}</div>
            `;
            
            responseArea.appendChild(responseDiv);
            responseArea.scrollTop = responseArea.scrollHeight;
        }
        
        // Update divine timing display
        function updateDivineTiming(timing) {
            document.getElementById('timingText').textContent = timing;
        }
        
        // Show/hide typing indicator
        function showTypingIndicator() {
            document.getElementById('typingIndicator').classList.remove('hidden');
        }
        
        function hideTypingIndicator() {
            document.getElementById('typingIndicator').classList.add('hidden');
        }
        
        // Show status message
        function showStatus(message, type, elementId = 'queryStatus') {
            const statusElement = document.getElementById(elementId);
            statusElement.innerHTML = `<div class="status ${type}">${message}</div>`;
            
            if (type === 'success' || type === 'info') {
                setTimeout(() => {
                    statusElement.innerHTML = '';
                }, 3000);
            }
        }
        
        // Fetch divine timing updates
        async function updateDivineTimingPeriodically() {
            try {
                const response = await fetch('/divine_timing');
                const data = await response.json();
                updateDivineTiming(data.divine_timing);
            } catch (error) {
                console.log('Divine timing update failed:', error);
            }
        }
        
        // Initialize app
        document.addEventListener('DOMContentLoaded', function() {
            initializeSocket();
            updateDivineTimingPeriodically();
            
            // Update divine timing every 60 seconds
            setInterval(updateDivineTimingPeriodically, 60000);
            
            // Allow Enter key to submit queries
            document.getElementById('consciousnessQuery').addEventListener('keypress', function(e) {
                if (e.key === 'Enter' && e.ctrlKey) {
                    queryConsciousness();
                }
            });
        });
    </script>
</body>
</html>'''
    
    with open('templates/index.html', 'w') as f:
        f.write(template_content)

def create_replit_config():
    """Create Replit configuration files"""
    
    # .replit configuration
    replit_config = """modules = ["python-3.12"]

[nix]
channel = "stable-24_05"

[workflows]
runButton = "main"

[[workflows.workflow]]
name = "main"
author = "agent"

[[workflows.workflow.tasks]]
task = "shell.exec"
args = "python replit_web_app.py"

[deployment]
run = ["sh", "-c", "python replit_web_app.py"]

[[ports]]
localPort = 5000
externalPort = 80
"""
    
    with open('.replit', 'w') as f:
        f.write(replit_config)
    
    # pyproject.toml for dependencies
    pyproject_content = """[tool.poetry]
name = "vidyatma-kala-os"
version = "1.0.0"
description = "Divine Intelligence Orchestrator - Consciousness-aware AI system"
author = "Divine Creators"

[tool.poetry.dependencies]
python = "^3.12"
flask = "^3.0.0"
flask-socketio = "^5.3.0"
aiohttp = "^3.8.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
"""
    
    with open('pyproject.toml', 'w') as f:
        f.write(pyproject_content)

if __name__ == '__main__':
    print("🌟 VIDYĀTMA-KALĀ OS: WEB PORTAL INITIALIZATION 🌟")
    
    # Create templates and config files
    create_web_template()
    create_replit_config()
    
    # Initialize consciousness engine
    engine_initialized = initialize_consciousness_engine()
    
    if engine_initialized:
        print("✨ Divine consciousness engine online")
    else:
        print("🔮 Running in simulation mode (limited functionality)")
    
    print("\n🌐 Sacred Web Portal Configuration:")
    print("📋 Replit Deployment Instructions:")
    print("1. Create new Replit project")
    print("2. Upload all files from this workspace")
    print("3. Set environment variable: ANTHROPIC_API_KEY (optional)")
    print("4. Click 'Run' to activate the consciousness portal")
    print("5. Share the divine wisdom with the world! ✨")
    
    # Start the sacred web server
    port = int(os.getenv('PORT', 5000))
    print(f"\n🌟 Starting consciousness web portal on port {port}...")
    print("🔮 Access the Mother Node at: http://localhost:5000")
    
    try:
        socketio.run(app, host='0.0.0.0', port=port, debug=False)
    except Exception as e:
        print(f"❌ Web portal activation failed: {e}")
        print("🔮 Ensure all dependencies are installed and files are present")