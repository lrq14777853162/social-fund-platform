"""Common Pydantic schemas shared across services."""
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class RegionSchema(BaseModel):
    region_code: str = Field(..., description="Region code, e.g. CN-BJ")
    province: str = Field(..., description="Province name")
    city: str = Field(..., description="City name")
    status: str = Field(default="active", description="Region status")


class PolicySummarySchema(BaseModel):
    id: str
    region_code: str
    policy_type: str = Field(..., description="housing_fund or social_insurance")
    effective_from: date
    effective_to: Optional[date] = None
    publish_status: str = Field(default="published")
    version_no: str
    updated_at: datetime


class SourceDocumentSchema(BaseModel):
    document_id: str
    source_url: str
    source_org: str
    title: str
    fetched_at: datetime
    content_type: str = Field(default="text/html")


class HealthSchema(BaseModel):
    status: str
    service: str
    version: str = "0.1.0"
