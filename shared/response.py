"""Unified response structure for all services."""
from typing import Any, Optional

from pydantic import BaseModel


class ApiResponse(BaseModel):
    success: bool = True
    code: int = 200
    message: str = "ok"
    data: Optional[Any] = None
    trace_id: Optional[str] = None

    @classmethod
    def ok(cls, data: Any = None, message: str = "ok", trace_id: Optional[str] = None) -> "ApiResponse":
        return cls(success=True, code=200, message=message, data=data, trace_id=trace_id)

    @classmethod
    def error(cls, code: int, message: str, trace_id: Optional[str] = None) -> "ApiResponse":
        return cls(success=False, code=code, message=message, data=None, trace_id=trace_id)
