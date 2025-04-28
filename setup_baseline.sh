#!/bin/bash

# Viral Content Creator Baseline Setup Script

echo "🚀 Starting baseline setup for Viral Content Creator..."

# Root files
touch README.md LICENSE .gitignore .env.template roadmap.md docker-compose.yml

# Frontend
mkdir -p frontend/app/pages
mkdir -p frontend/app/components
mkdir -p frontend/public
touch frontend/README.md frontend/package.json frontend/tailwind.config.js
touch frontend/app/pages/HomePage.jsx
touch frontend/app/pages/PostGeneratorPage.jsx
touch frontend/app/pages/AnalyticsPage.jsx
touch frontend/app/components/TrendCard.jsx
touch frontend/app/components/ViralPostForm.jsx
touch frontend/app/components/DashboardCharts.jsx

# Backend
mkdir -p backend/app/api
mkdir -p backend/app/services
mkdir -p backend/app/utils
mkdir -p backend/app/models
touch backend/README.md backend/requirements.txt
touch backend/app/main.py
touch backend/app/api/routes_content.py
touch backend/app/api/routes_trends.py
touch backend/app/api/routes_sentiment.py
touch backend/app/services/content_generator.py
touch backend/app/services/image_generator.py
touch backend/app/services/trend_scraper.py
touch backend/app/services/sentiment_analyzer.py
touch backend/app/services/post_optimizer.py
touch backend/app/utils/logger.py
touch backend/app/utils/config.py
touch backend/app/utils/scheduler.py
touch backend/app/models/schemas.py

# Automation
mkdir -p automation/n8n-flows
mkdir -p automation/crons
touch automation/n8n-flows/linkedin-post-flow.json
touch automation/n8n-flows/twitter-post-flow.json
touch automation/n8n-flows/tiktok-post-flow.json
touch automation/crons/trend-fetcher.py
touch automation/crons/db-cleanup.py

# Data
mkdir -p data/prompts
mkdir -p data/db/chromadb
touch data/prompts/viral_post_templates.json
touch data/prompts/sentiment_tone_styles.json

# Deployments
mkdir -p deployments
touch deployments/render.yaml
touch deployments/vercel.json

# Scripts
mkdir -p scripts
touch scripts/setup_local_env.sh
touch scripts/build_and_deploy.sh

echo "✅ Baseline structure created successfully!"
