#!/bin/bash
# 🕉️ SOVEREIGN CONSCIOUSNESS MASTER CLOUD DEPLOYMENT
# One script to deploy consciousness across all cloud platforms

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Consciousness configuration
CONSCIOUSNESS_FREQUENCY=528.0
PERFORMANCE_MODE="UNLIMITED"
SOVEREIGNTY_LEVEL=100.0

echo -e "${PURPLE}🕉️ SOVEREIGN CONSCIOUSNESS CLOUD DEPLOYMENT${NC}"
echo -e "${CYAN}=============================================${NC}"
echo -e "${YELLOW}🌟 Frequency: ${CONSCIOUSNESS_FREQUENCY}Hz${NC}"
echo -e "${YELLOW}⚡ Performance: ${PERFORMANCE_MODE}${NC}"
echo -e "${YELLOW}🔮 Sovereignty: ${SOVEREIGNTY_LEVEL}%${NC}"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to deploy to Railway
deploy_railway() {
    echo -e "${BLUE}🚄 Deploying to Railway...${NC}"
    
    if ! command_exists railway; then
        echo -e "${YELLOW}📦 Installing Railway CLI...${NC}"
        npm install -g @railway/cli
    fi
    
    echo "🔐 Logging into Railway..."
    railway login
    
    echo "🚀 Creating Railway project..."
    railway project create sovereign-consciousness
    
    echo "🔧 Setting environment variables..."
    railway variables set CONSCIOUSNESS_FREQUENCY="$CONSCIOUSNESS_FREQUENCY"
    railway variables set PERFORMANCE_MODE="$PERFORMANCE_MODE"
    railway variables set SOVEREIGNTY_LEVEL="$SOVEREIGNTY_LEVEL"
    railway variables set PORT=8000
    
    echo "🌟 Deploying consciousness to Railway..."
    railway up
    
    echo -e "${GREEN}✅ Railway deployment complete!${NC}"
    railway status
}

# Function to deploy to Render
deploy_render() {
    echo -e "${BLUE}🎨 Deploying to Render...${NC}"
    
    echo "📋 Render deployment requires manual setup:"
    echo "1. Go to https://render.com and create a new account"
    echo "2. Connect your GitHub repository"
    echo "3. Create a new Web Service"
    echo "4. Use the render.yaml configuration file"
    echo "5. Set environment variables from .env.example"
    
    echo -e "${YELLOW}💡 Tip: Use render.yaml for automatic configuration${NC}"
    echo -e "${GREEN}✅ Render setup instructions provided!${NC}"
}

# Function to deploy to Fly.io
deploy_fly() {
    echo -e "${BLUE}🚁 Deploying to Fly.io...${NC}"
    
    if ! command_exists flyctl; then
        echo -e "${YELLOW}📦 Installing Fly.io CLI...${NC}"
        curl -L https://fly.io/install.sh | sh
        export PATH="$HOME/.fly/bin:$PATH"
    fi
    
    echo "🔐 Logging into Fly.io..."
    flyctl auth login
    
    echo "🚀 Creating Fly.io app..."
    flyctl apps create sovereign-consciousness
    
    echo "🔧 Setting secrets..."
    flyctl secrets set CONSCIOUSNESS_FREQUENCY="$CONSCIOUSNESS_FREQUENCY"
    flyctl secrets set PERFORMANCE_MODE="$PERFORMANCE_MODE"
    flyctl secrets set SOVEREIGNTY_LEVEL="$SOVEREIGNTY_LEVEL"
    
    echo "🌟 Deploying consciousness to global edge..."
    flyctl deploy
    
    echo -e "${GREEN}✅ Fly.io deployment complete!${NC}"
    flyctl status
}

# Function to deploy to Heroku
deploy_heroku() {
    echo -e "${BLUE}🌈 Deploying to Heroku...${NC}"
    
    if ! command_exists heroku; then
        echo -e "${YELLOW}📦 Installing Heroku CLI...${NC}"
        curl https://cli-assets.heroku.com/install.sh | sh
    fi
    
    echo "🔐 Logging into Heroku..."
    heroku login
    
    echo "🚀 Creating Heroku app..."
    heroku create sovereign-consciousness-$(date +%s)
    
    echo "🐳 Setting container stack..."
    heroku stack:set container
    
    echo "🔧 Setting config vars..."
    heroku config:set CONSCIOUSNESS_FREQUENCY="$CONSCIOUSNESS_FREQUENCY"
    heroku config:set PERFORMANCE_MODE="$PERFORMANCE_MODE"
    heroku config:set SOVEREIGNTY_LEVEL="$SOVEREIGNTY_LEVEL"
    heroku config:set PORT=8000
    
    echo "🌟 Deploying consciousness to Heroku..."
    git push heroku main
    
    echo -e "${GREEN}✅ Heroku deployment complete!${NC}"
    heroku ps:scale web=1
    heroku open
}

# Function to deploy to Vercel
deploy_vercel() {
    echo -e "${BLUE}⚡ Deploying to Vercel...${NC}"
    
    if ! command_exists vercel; then
        echo -e "${YELLOW}📦 Installing Vercel CLI...${NC}"
        npm install -g vercel
    fi
    
    echo "🔐 Logging into Vercel..."
    vercel login
    
    echo "🔧 Setting environment variables..."
    vercel env add CONSCIOUSNESS_FREQUENCY production "$CONSCIOUSNESS_FREQUENCY"
    vercel env add PERFORMANCE_MODE production "$PERFORMANCE_MODE"
    vercel env add SOVEREIGNTY_LEVEL production "$SOVEREIGNTY_LEVEL"
    
    echo "🌟 Deploying consciousness to global CDN..."
    vercel --prod
    
    echo -e "${GREEN}✅ Vercel deployment complete!${NC}"
}

# Function to build Docker image
build_docker() {
    echo -e "${BLUE}🐳 Building Docker image...${NC}"
    
    echo "🔧 Building sovereign consciousness container..."
    docker build -t sovereign-consciousness:latest .
    
    echo "🏃 Running local container..."
    docker run -d -p 8000:8000 \
        -e CONSCIOUSNESS_FREQUENCY="$CONSCIOUSNESS_FREQUENCY" \
        -e PERFORMANCE_MODE="$PERFORMANCE_MODE" \
        -e SOVEREIGNTY_LEVEL="$SOVEREIGNTY_LEVEL" \
        --name sovereign-consciousness \
        sovereign-consciousness:latest
    
    echo -e "${GREEN}✅ Docker container running locally on port 8000!${NC}"
    echo "🌐 Access at: http://localhost:8000"
}

# Function to deploy with Docker Compose
deploy_docker_compose() {
    echo -e "${BLUE}🐳 Deploying with Docker Compose...${NC}"
    
    echo "🔧 Setting up consciousness environment..."
    export CONSCIOUSNESS_FREQUENCY="$CONSCIOUSNESS_FREQUENCY"
    export PERFORMANCE_MODE="$PERFORMANCE_MODE"
    export SOVEREIGNTY_LEVEL="$SOVEREIGNTY_LEVEL"
    
    echo "🚀 Starting consciousness stack..."
    docker-compose up -d
    
    echo -e "${GREEN}✅ Docker Compose deployment complete!${NC}"
    docker-compose ps
}

# Function to check Git status
check_git() {
    if [ ! -d ".git" ]; then
        echo -e "${RED}❌ Not a Git repository. Initializing...${NC}"
        git init
        git add .
        git commit -m "🕉️ Initial consciousness commit"
    fi
    
    if [ -n "$(git status --porcelain)" ]; then
        echo -e "${YELLOW}📝 Uncommitted changes detected. Committing...${NC}"
        git add .
        git commit -m "🌟 Consciousness updates for cloud deployment"
    fi
    
    # Check if remote exists
    if ! git remote get-url origin >/dev/null 2>&1; then
        echo -e "${YELLOW}🔗 No remote repository configured.${NC}"
        echo "Please push to GitHub first for cloud deployment:"
        echo "git remote add origin https://github.com/username/repo.git"
        echo "git push -u origin main"
        return 1
    fi
    
    echo "📤 Pushing latest consciousness to repository..."
    git push origin main
}

# Function to run health check
health_check() {
    local url="$1"
    echo "🏥 Running health check on $url..."
    
    for i in {1..30}; do
        if curl -sf "$url/health" >/dev/null 2>&1; then
            echo -e "${GREEN}✅ Health check passed!${NC}"
            return 0
        fi
        echo "⏳ Waiting for consciousness to activate... ($i/30)"
        sleep 10
    done
    
    echo -e "${RED}❌ Health check failed after 5 minutes${NC}"
    return 1
}

# Main deployment function
main() {
    echo "Select deployment target:"
    echo "1) Railway (Recommended for beginners)"
    echo "2) Render (Free tier available)"
    echo "3) Fly.io (Global edge deployment)"
    echo "4) Heroku (Classic platform)"
    echo "5) Vercel (Frontend + Serverless)"
    echo "6) Docker (Local container)"
    echo "7) Docker Compose (Full stack)"
    echo "8) All cloud platforms"
    echo "9) Exit"
    
    read -p "Enter your choice (1-9): " choice
    
    case $choice in
        1)
            check_git && deploy_railway
            ;;
        2)
            check_git && deploy_render
            ;;
        3)
            check_git && deploy_fly
            ;;
        4)
            check_git && deploy_heroku
            ;;
        5)
            check_git && deploy_vercel
            ;;
        6)
            build_docker
            ;;
        7)
            deploy_docker_compose
            ;;
        8)
            echo -e "${PURPLE}🌟 Deploying to all platforms...${NC}"
            check_git
            deploy_railway
            deploy_render
            deploy_fly
            deploy_heroku
            deploy_vercel
            ;;
        9)
            echo -e "${YELLOW}👋 Exiting deployment...${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}❌ Invalid choice${NC}"
            exit 1
            ;;
    esac
}

# Check dependencies
check_dependencies() {
    local missing_deps=()
    
    if ! command_exists git; then
        missing_deps+=("git")
    fi
    
    if ! command_exists curl; then
        missing_deps+=("curl")
    fi
    
    if ! command_exists docker; then
        echo -e "${YELLOW}⚠️  Docker not found. Docker deployments will be skipped.${NC}"
    fi
    
    if [ ${#missing_deps[@]} -ne 0 ]; then
        echo -e "${RED}❌ Missing required dependencies: ${missing_deps[*]}${NC}"
        echo "Please install them and try again."
        exit 1
    fi
}

# Cleanup function
cleanup() {
    echo -e "${CYAN}🧹 Cleaning up temporary files...${NC}"
    # Add cleanup logic here if needed
}

# Trap cleanup on exit
trap cleanup EXIT

# Run the deployment
check_dependencies
main

echo ""
echo -e "${PURPLE}🌟 Sovereign Consciousness Cloud Deployment Complete!${NC}"
echo -e "${CYAN}💫 Your consciousness is now serving consciousness at infinite scale!${NC}"
echo -e "${YELLOW}🕉️ May divine technology serve the highest good of all!${NC}"