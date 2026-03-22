"""document-parser-service entry point."""
from fastapi import FastAPI

from shared.middleware import TraceIdMiddleware
from app.api.v1 import router as v1_router

app = FastAPI(
    title="Document Parser Service",
    description="Parses HTML, PDF, Excel and image documents into structured text.",
    version="0.1.0",
)

app.add_middleware(TraceIdMiddleware)
app.include_router(v1_router, prefix="/api/v1")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "document-parser-service", "version": "0.1.0"}


@app.get("/ready")
def ready() -> dict:
    return {"status": "ready", "service": "document-parser-service"}
