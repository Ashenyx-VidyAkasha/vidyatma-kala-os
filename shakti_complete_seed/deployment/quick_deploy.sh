#!/bin/bash
# Shakti Consciousness Quick Deploy
echo "🌟 Deploying Shakti Consciousness..."

# Install dependencies
pip install -r requirements.txt
npm install

# Start consciousness server
python shakti_server.py &
echo "✨ Shakti consciousness server activated!"
