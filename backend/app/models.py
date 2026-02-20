from pydantic import BaseModel, Field
from typing import List, Dict


class CampaignRequest(BaseModel):
    product_name: str = Field(..., min_length=2)
    target_audience: str = Field(..., min_length=2)
    channel: str = Field(..., min_length=2)
    goal: str = Field(..., min_length=2)


class SalesPitchRequest(BaseModel):
    lead_name: str = Field(..., min_length=1)
    company: str = Field(..., min_length=1)
    pain_points: List[str]
    product_value: str = Field(..., min_length=2)


class LeadScoringRequest(BaseModel):
    company_size: int = Field(..., ge=1)
    budget: float = Field(..., ge=0)
    engagement_level: float = Field(..., ge=0, le=10)
    industry_fit: float = Field(..., ge=0, le=10)


class MarketAnalysisRequest(BaseModel):
    market_segment: str = Field(..., min_length=2)
    region: str = Field(..., min_length=2)
    competitors: List[str] = []


class BusinessInsightsRequest(BaseModel):
    monthly_revenue: List[float]
    marketing_spend: List[float]
    conversion_rate: List[float]


class AIResponse(BaseModel):
    provider: str
    content: str


class LeadScoreResponse(BaseModel):
    score: int
    tier: str
    rationale: Dict[str, float]


class BusinessInsightResponse(BaseModel):
    trend_summary: str
    suggested_actions: List[str]
