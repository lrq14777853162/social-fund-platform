"""v1 router for collector-service."""
from fastapi import APIRouter

from app.api.v1.discovery import router as discovery_router

router = APIRouter()
router.include_router(discovery_router, prefix="/discovery", tags=["Discovery"])
