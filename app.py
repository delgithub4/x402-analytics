from fastapi import FastAPI

from routes.analytics import router as analytics_router
from routes.health import router as health_router

app = FastAPI(
    title="x402-analytics",
    version="1.0.0"
)

app.include_router(analytics_router)
app.include_router(health_router)


@app.get("/")
def home():

    return {

        "service":"x402-analytics",

        "status":"running"

    }
