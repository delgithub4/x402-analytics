from fastapi import APIRouter

from services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

service = AnalyticsService()


@router.get("/")
def analytics():

    return service.overview()
