"""Middleware shared across services (e.g., TraceID injection)."""
import uuid
from typing import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

TRACE_ID_HEADER = "X-Trace-Id"


class TraceIdMiddleware(BaseHTTPMiddleware):
    """Injects a unique trace ID into every request and response."""

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        trace_id = request.headers.get(TRACE_ID_HEADER) or str(uuid.uuid4())
        request.state.trace_id = trace_id
        response = await call_next(request)
        response.headers[TRACE_ID_HEADER] = trace_id
        return response
