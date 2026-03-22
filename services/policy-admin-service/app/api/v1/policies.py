"""Policies endpoint – returns mock current policy data."""
from datetime import date, datetime
from typing import List

from fastapi import APIRouter, Request

from shared.response import ApiResponse
from shared.schemas import PolicySummarySchema

router = APIRouter()

_MOCK_POLICIES: List[PolicySummarySchema] = [
    PolicySummarySchema(
        id="POL-001",
        region_code="CN-BJ",
        policy_type="housing_fund",
        effective_from=date(2025, 7, 1),
        publish_status="published",
        version_no="2025-v1",
        updated_at=datetime(2025, 6, 28, 10, 0, 0),
    ),
    PolicySummarySchema(
        id="POL-002",
        region_code="CN-SH",
        policy_type="social_insurance",
        effective_from=date(2025, 7, 1),
        publish_status="published",
        version_no="2025-v1",
        updated_at=datetime(2025, 6, 30, 9, 0, 0),
    ),
    PolicySummarySchema(
        id="POL-003",
        region_code="CN-GD-SZ",
        policy_type="housing_fund",
        effective_from=date(2025, 7, 1),
        publish_status="published",
        version_no="2025-v1",
        updated_at=datetime(2025, 7, 1, 8, 0, 0),
    ),
]


@router.get("/current", response_model=ApiResponse)
def get_current_policies(request: Request) -> ApiResponse:
    trace_id: str = getattr(request.state, "trace_id", None)
    return ApiResponse.ok(
        data=[p.model_dump() for p in _MOCK_POLICIES],
        trace_id=trace_id,
    )
