from fastapi import FastAPI
from app.api import routes_content, routes_trends, routes_sentiment
from app.api.routes_health import router as health_router  # 👈 Add this line

app = FastAPI()

# Include routers
app.include_router(routes_content.router, prefix="/content", tags=["Content"])
app.include_router(routes_trends.router, prefix="/trends", tags=["Trends"])
app.include_router(routes_sentiment.router, prefix="/sentiment", tags=["Sentiment"])
app.include_router(health_router, tags=["Health"])  # 👈 Add this line
