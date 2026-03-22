"""ai-extract-service entry point."""
from fastapi import FastAPI

from shared.middleware import TraceIdMiddleware
from app.api.v1 import router as v1_router

app = FastAPI(
    title="AI Extract Service",
    description="Extracts structured policy fields from parsed document text using rule + AI pipelines.",
    version="0.1.0",
)

app.add_middleware(TraceIdMiddleware)
app.include_router(v1_router, prefix="/api/v1")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "ai-extract-service", "version": "0.1.0"}


@app.get("/ready")
def ready() -> dict:
    return {"status": "ready", "service": "ai-extract-service"}
