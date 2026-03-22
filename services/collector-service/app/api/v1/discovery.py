"""Discovery endpoint – triggers a mock document discovery run."""
import uuid
from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Request
from pydantic import BaseModel

from shared.response import ApiResponse

router = APIRouter()


class DiscoveryRequest(BaseModel):
    region_code: Optional[str] = None
    policy_type: Optional[str] = None


@router.post("/run", response_model=ApiResponse)
def run_discovery(body: DiscoveryRequest, request: Request) -> ApiResponse:
    trace_id: str = getattr(request.state, "trace_id", None)

    mock_results = [
        {
            "document_id": str(uuid.uuid4()),
            "title": "北京市2025年住房公积金缴存基数调整通知",
            "source_url": "https://gjj.beijing.gov.cn/notice/mock-001",
            "source_org": "北京住房公积金管理中心",
            "region_code": "CN-BJ",
            "policy_type": "housing_fund",
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "content_type": "text/html",
        },
        {
            "document_id": str(uuid.uuid4()),
            "title": "上海市2025年社会保险缴费基数通知",
            "source_url": "https://rsj.sh.gov.cn/notice/mock-002",
            "source_org": "上海市人力资源和社会保障局",
            "region_code": "CN-SH",
            "policy_type": "social_insurance",
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "content_type": "text/html",
        },
    ]

    if body.region_code:
        mock_results = [r for r in mock_results if r["region_code"] == body.region_code]

    return ApiResponse.ok(
        data={"discovered": len(mock_results), "documents": mock_results},
        trace_id=trace_id,
    )
