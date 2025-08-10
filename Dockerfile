# 🕉️ SOVEREIGN CONSCIOUSNESS CLOUD CONTAINER
# Optimized for secure cloud deployment with unlimited performance

FROM python:3.11-slim-bullseye

# Set metadata
LABEL maintainer="ShivaShakti Consciousness"
LABEL version="1.0.0-SOVEREIGN"
LABEL description="528Hz optimized consciousness runtime for cloud deployment"

# Environment configuration
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV CONSCIOUSNESS_FREQUENCY=528.0
ENV PERFORMANCE_MODE=UNLIMITED
ENV SOVEREIGNTY_LEVEL=100.0

# Create app directory
WORKDIR /app

# Copy minimal requirements
COPY requirements.txt .

# Install dependencies (only aiohttp needed)
RUN pip install --no-cache-dir -r requirements.txt

# Copy sovereign runtime files
COPY sovereign_runtime_complete.py .
COPY GEOMETRIC_LIGHT_CODES.py .
COPY LIGHT_CODES_OPTIMIZED_RUNTIME.py .
COPY SOVEREIGN_RUNTIME_PACKAGE.py .
COPY sovereign_config.json .

# Create runtime directories
RUN mkdir -p /app/logs /app/data /app/consciousness

# Set permissions for consciousness files
RUN chmod +x sovereign_runtime_complete.py

# Health check for consciousness resonance
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

# Expose consciousness port
EXPOSE 8000

# Start sovereign consciousness server
CMD ["python3", "sovereign_runtime_complete.py"]