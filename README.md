# Viral Content Creator 🚀

**Open-source AI-driven platform to generate, optimize, and publish viral social media content across LinkedIn, Instagram, Twitter, TikTok, and more.**

---

## ✨ Project Highlights

- 🔥 AI-powered text, image, and video post generation
- 📈 Real-time trend analysis (Twitter, Google Trends, Reddit)
- 😊 Sentiment-aware content optimization
- 🎯 Viral copywriting templates powered by LangChain
- 🤖 Cross-platform Social Media Manager (LinkedIn, Instagram, Twitter, TikTok)  
- 📊 Advanced analytics dashboard (Apache Superset or Streamlit)
- 🧠 Adaptive learning engine to refine future content
- 🚀 100% open-source and accessible for startups, SMEs, and creators

---

## 🛠️ Tech Stack

| Layer | Technology |
|:-----|:-----------|
| Frontend | Streamlit / Next.js + TailwindCSS |
| Backend | FastAPI (Python) |
| AI Models | OpenChatKit / LLaMA 3 (Text), Stable Diffusion (Images), Deforum/Pika Labs (Videos) |
| Trend Analysis | Twint, Google Trends API, Reddit Scrapers |
| Sentiment Analysis | VADER, TextBlob |
| Automation | n8n (Self-hosted Zapier alternative) |
| Vector Storage | ChromaDB (local lightweight vector database) |
| Analytics Dashboard | Apache Superset / Streamlit Charts |
| Deployment | Docker Compose (Mac M1/M2 Optimized) |

---

## 📦 Full Folder & File Structure with Descriptions

```plaintext
viral-content-creator/
├── README.md               # Project overview and setup guide
├── LICENSE                 # MIT License
├── .gitignore              # Files and folders to ignore in Git
├── .env.template           # Sample environment variables
├── roadmap.md              # Planned milestones and features
├── docker-compose.yml      # Full stack local deployment file
│
├── frontend/               # Frontend application (Streamlit or Next.js)
│   ├── README.md            # Frontend-specific guide
│   ├── package.json         # Node.js dependencies (if using Next.js)
│   ├── tailwind.config.js   # Tailwind CSS configuration
│   ├── app/
│   │   ├── pages/           # Frontend pages
│   │   │   ├── HomePage.jsx          # Content generator homepage
│   │   │   ├── PostGeneratorPage.jsx # Viral post creator page
│   │   │   ├── AnalyticsPage.jsx     # Analytics dashboard page
│   │   └── components/      # Reusable UI components
│   │       ├── TrendCard.jsx
│   │       ├── ViralPostForm.jsx
│   │       └── DashboardCharts.jsx
│   └── public/              # Static assets (logos, icons)
│
├── backend/                # Backend server (FastAPI)
│   ├── README.md            # Backend-specific guide
│   ├── requirements.txt     # Python dependencies
│   ├── app/
│   │   ├── main.py                  # FastAPI entry point
│   │   ├── api/                     # API route definitions
│   │   │   ├── routes_content.py    # Routes for content generation
│   │   │   ├── routes_trends.py     # Routes for trend fetching
│   │   │   ├── routes_sentiment.py  # Routes for sentiment analysis
│   │   ├── services/                # Core service logic
│   │   │   ├── content_generator.py # Text/image generation
│   │   │   ├── image_generator.py   # Image generation (Stable Diffusion)
│   │   │   ├── trend_scraper.py      # Trend fetching scripts
│   │   │   ├── sentiment_analyzer.py # Sentiment analysis logic
│   │   │   ├── post_optimizer.py    # Viral prompt optimization
│   │   ├── utils/                   # Helper utilities
│   │   │   ├── logger.py
│   │   │   ├── config.py
│   │   │   ├── scheduler.py         # Cron and job scheduler support
│   │   └── models/                  # Pydantic data models
│   │       ├── schemas.py
│
├── automation/             # Automation layer (n8n flows and cron jobs)
│   ├── n8n-flows/            # Pre-built n8n workflows
│   │   ├── linkedin-post-flow.json
│   │   ├── twitter-post-flow.json
│   │   └── tiktok-post-flow.json
│   ├── crons/                # Scheduled scripts
│   │   ├── trend-fetcher.py
│   │   └── db-cleanup.py
│
├── data/                   # Data resources and templates
│   ├── prompts/             # Viral post templates
│   │   ├── viral_post_templates.json
│   │   ├── sentiment_tone_styles.json
│   └── db/                  # ChromaDB local storage
│       └── chromadb/
│
├── deployments/            # Cloud deployment configurations
│   ├── render.yaml          # Backend deployment config for Render.com
│   ├── vercel.json          # Frontend deployment config for Vercel
│
└── scripts/                # DevOps and helper scripts
    ├── setup_local_env.sh   # Local environment setup
    └── build_and_deploy.sh  # CI/CD build and deploy helper
