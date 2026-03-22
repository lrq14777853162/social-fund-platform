"""v1 router aggregating all endpoints."""
from fastapi import APIRouter

from app.api.v1.regions import router as regions_router
from app.api.v1.policies import router as policies_router

router = APIRouter()
router.include_router(regions_router, prefix="/regions", tags=["Regions"])
router.include_router(policies_router, prefix="/policies", tags=["Policies"])
