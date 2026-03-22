"""Extract endpoint – returns mock AI field extraction results."""
from typing import List, Optional

from fastapi import APIRouter, Request
from pydantic import BaseModel

from shared.response import ApiResponse

router = APIRouter()


class ExtractRequest(BaseModel):
    document_id: str
    parsed_text: Optional[str] = None
    chunks: Optional[List[dict]] = None


@router.post("/fields", response_model=ApiResponse)
def extract_fields(body: ExtractRequest, request: Request) -> ApiResponse:
    trace_id: str = getattr(request.state, "trace_id", None)

    mock_result = {
        "document_id": body.document_id,
        "fields": {
            "region_code": "CN-BJ",
            "policy_type": "housing_fund",
            "effective_from": "2025-07-01",
            "base_min": 2420,
            "base_max": 35326,
            "employer_ratio_min": 5,
            "employer_ratio_max": 12,
            "employee_ratio_min": 5,
            "employee_ratio_max": 12,
            "source_org": "北京住房公积金管理中心",
        },
        "confidence": 0.92,
        "evidences": [
            {
                "field": "base_min",
                "text": "缴存基数下限为2420元",
                "chunk_id": "c1",
                "page": 1,
            },
            {
                "field": "base_max",
                "text": "上限为35326元",
                "chunk_id": "c1",
                "page": 1,
            },
        ],
    }

    return ApiResponse.ok(data=mock_result, trace_id=trace_id)
