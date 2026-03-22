"""Parse endpoint – returns mock document parsing results."""
from typing import Optional

from fastapi import APIRouter, Request
from pydantic import BaseModel

from shared.response import ApiResponse

router = APIRouter()


class ParseRequest(BaseModel):
    document_id: str
    source_url: Optional[str] = None
    content_type: Optional[str] = "text/html"


@router.post("/document", response_model=ApiResponse)
def parse_document(body: ParseRequest, request: Request) -> ApiResponse:
    trace_id: str = getattr(request.state, "trace_id", None)

    mock_result = {
        "document_id": body.document_id,
        "content_type": body.content_type,
        "parsed_text": (
            "北京市2025年住房公积金缴存基数调整通知\n"
            "根据本市职工工资增长情况，调整2025年度住房公积金缴存基数上下限。"
            "缴存基数下限为2420元，上限为35326元。"
        ),
        "tables": [
            {
                "table_id": "t1",
                "headers": ["缴存基数类型", "金额（元）"],
                "rows": [
                    ["下限", "2420"],
                    ["上限", "35326"],
                ],
            }
        ],
        "chunks": [
            {"chunk_id": "c1", "text": "缴存基数下限为2420元，上限为35326元。", "page": 1},
        ],
    }

    return ApiResponse.ok(data=mock_result, trace_id=trace_id)
