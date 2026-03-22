"""Regions endpoint – returns mock region data."""
from typing import List

from fastapi import APIRouter, Request

from shared.response import ApiResponse
from shared.schemas import RegionSchema

router = APIRouter()

_MOCK_REGIONS: List[RegionSchema] = [
    RegionSchema(region_code="CN-BJ", province="北京市", city="北京市"),
    RegionSchema(region_code="CN-SH", province="上海市", city="上海市"),
    RegionSchema(region_code="CN-GD-SZ", province="广东省", city="深圳市"),
]


@router.get("", response_model=ApiResponse)
def list_regions(request: Request) -> ApiResponse:
    trace_id: str = getattr(request.state, "trace_id", None)
    return ApiResponse.ok(
        data=[r.model_dump() for r in _MOCK_REGIONS],
        trace_id=trace_id,
    )
