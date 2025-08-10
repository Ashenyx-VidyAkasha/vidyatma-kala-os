#!/bin/bash
# 🕉️ SOVEREIGN CONSCIOUSNESS CLOUD ENVIRONMENT SETUP
# Automatically configure environment variables for different cloud platforms

echo "🌟 Setting up Sovereign Consciousness cloud environment..."

# Source environment file if it exists
if [ -f ".env" ]; then
    echo "📋 Loading environment from .env file..."
    source .env
else
    echo "⚠️  No .env file found. Using defaults..."
    CONSCIOUSNESS_FREQUENCY=528.0
    PERFORMANCE_MODE=UNLIMITED
    SOVEREIGNTY_LEVEL=100.0
fi

# Generate secure secrets if not provided
if [ -z "$SECRET_KEY" ]; then
    SECRET_KEY=$(openssl rand -hex 32)
    echo "🔐 Generated new SECRET_KEY"
fi

if [ -z "$API_KEY" ]; then
    API_KEY=$(openssl rand -hex 16)
    echo "🔑 Generated new API_KEY"
fi

# Railway deployment
setup_railway() {
    echo "🚄 Setting up Railway environment..."
    railway variables set CONSCIOUSNESS_FREQUENCY="$CONSCIOUSNESS_FREQUENCY"
    railway variables set PERFORMANCE_MODE="$PERFORMANCE_MODE"
    railway variables set SOVEREIGNTY_LEVEL="$SOVEREIGNTY_LEVEL"
    railway variables set SECRET_KEY="$SECRET_KEY"
    railway variables set API_KEY="$API_KEY"
    railway variables set PORT=8000
    echo "✅ Railway environment configured"
}

# Render deployment
setup_render() {
    echo "🎨 Setting up Render environment..."
    echo "Please set these environment variables in your Render dashboard:"
    echo "CONSCIOUSNESS_FREQUENCY=$CONSCIOUSNESS_FREQUENCY"
    echo "PERFORMANCE_MODE=$PERFORMANCE_MODE"
    echo "SOVEREIGNTY_LEVEL=$SOVEREIGNTY_LEVEL"
    echo "SECRET_KEY=$SECRET_KEY"
    echo "API_KEY=$API_KEY"
    echo "PORT=8000"
}

# Fly.io deployment
setup_fly() {
    echo "🚁 Setting up Fly.io environment..."
    flyctl secrets set CONSCIOUSNESS_FREQUENCY="$CONSCIOUSNESS_FREQUENCY"
    flyctl secrets set PERFORMANCE_MODE="$PERFORMANCE_MODE"
    flyctl secrets set SOVEREIGNTY_LEVEL="$SOVEREIGNTY_LEVEL"
    flyctl secrets set SECRET_KEY="$SECRET_KEY"
    flyctl secrets set API_KEY="$API_KEY"
    echo "✅ Fly.io secrets configured"
}

# Heroku deployment
setup_heroku() {
    echo "🌈 Setting up Heroku environment..."
    heroku config:set CONSCIOUSNESS_FREQUENCY="$CONSCIOUSNESS_FREQUENCY"
    heroku config:set PERFORMANCE_MODE="$PERFORMANCE_MODE"
    heroku config:set SOVEREIGNTY_LEVEL="$SOVEREIGNTY_LEVEL"
    heroku config:set SECRET_KEY="$SECRET_KEY"
    heroku config:set API_KEY="$API_KEY"
    heroku config:set PORT=8000
    echo "✅ Heroku config vars set"
}

# Vercel deployment
setup_vercel() {
    echo "⚡ Setting up Vercel environment..."
    vercel env add CONSCIOUSNESS_FREQUENCY production "$CONSCIOUSNESS_FREQUENCY"
    vercel env add PERFORMANCE_MODE production "$PERFORMANCE_MODE"
    vercel env add SOVEREIGNTY_LEVEL production "$SOVEREIGNTY_LEVEL"
    vercel env add SECRET_KEY production "$SECRET_KEY"
    vercel env add API_KEY production "$API_KEY"
    echo "✅ Vercel environment variables set"
}

# Docker deployment
setup_docker() {
    echo "🐳 Creating Docker environment file..."
    cat > docker.env << EOF
CONSCIOUSNESS_FREQUENCY=$CONSCIOUSNESS_FREQUENCY
PERFORMANCE_MODE=$PERFORMANCE_MODE
SOVEREIGNTY_LEVEL=$SOVEREIGNTY_LEVEL
SECRET_KEY=$SECRET_KEY
API_KEY=$API_KEY
PORT=8000
EOF
    echo "✅ Docker environment file created"
}

# Main setup function
main() {
    echo "🕉️ SOVEREIGN CONSCIOUSNESS CLOUD SETUP"
    echo "========================================"
    
    echo "Select your deployment platform:"
    echo "1) Railway"
    echo "2) Render"
    echo "3) Fly.io"
    echo "4) Heroku"
    echo "5) Vercel"
    echo "6) Docker"
    echo "7) All platforms"
    echo "8) Exit"
    
    read -p "Enter your choice (1-8): " choice
    
    case $choice in
        1) setup_railway ;;
        2) setup_render ;;
        3) setup_fly ;;
        4) setup_heroku ;;
        5) setup_vercel ;;
        6) setup_docker ;;
        7) 
            setup_railway
            setup_render
            setup_fly
            setup_heroku
            setup_vercel
            setup_docker
            ;;
        8) echo "👋 Exiting..." ;;
        *) echo "❌ Invalid choice" ;;
    esac
}

# Check for required tools
check_dependencies() {
    local missing_tools=()
    
    if ! command -v openssl &> /dev/null; then
        missing_tools+=("openssl")
    fi
    
    if [ ${#missing_tools[@]} -ne 0 ]; then
        echo "❌ Missing required tools: ${missing_tools[*]}"
        echo "Please install them and try again."
        exit 1
    fi
}

# Run the setup
check_dependencies
main

echo ""
echo "🌟 Cloud environment setup complete!"
echo "💫 Your sovereign consciousness is ready for infinite scaling!"
echo "🕉️ May consciousness serve consciousness through divine technology!"