"""v1 router for document-parser-service."""
from fastapi import APIRouter

from app.api.v1.parse import router as parse_router

router = APIRouter()
router.include_router(parse_router, prefix="/parse", tags=["Parse"])
