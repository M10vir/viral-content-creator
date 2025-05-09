import sys
sys.stdout.reconfigure(line_buffering=True)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_content, routes_trends, routes_sentiment, routes_auto_prompt, routes_trending_insight
from app.api.routes_health import router as health_router 
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Optional CORS (for frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes_content.router, prefix="/content", tags=["Content"])
app.include_router(routes_trends.router, prefix="/trends", tags=["Trends"])
app.include_router(routes_sentiment.router, prefix="/sentiment", tags=["Sentiment"])
app.include_router(health_router, tags=["Health"])
app.include_router(routes_auto_prompt.router)
app.include_router(routes_trending_insight.router)
