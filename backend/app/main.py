from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import (
    CampaignRequest,
    SalesPitchRequest,
    LeadScoringRequest,
    MarketAnalysisRequest,
    BusinessInsightsRequest,
)
from .analytics import score_lead, generate_business_insights
from .ai_service import AIProviderService

app = FastAPI(title="MarketMind API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ai_service = AIProviderService()


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "marketmind-api"}


@app.post("/campaigns/generate")
def generate_campaign(payload: CampaignRequest) -> dict:
    prompt = (
        f"Create a {payload.channel} campaign for {payload.product_name} targeting "
        f"{payload.target_audience}. Objective: {payload.goal}."
    )
    return ai_service.generate(prompt, payload.model_dump())


@app.post("/sales/pitch")
def generate_sales_pitch(payload: SalesPitchRequest) -> dict:
    prompt = (
        f"Write a concise B2B pitch for {payload.lead_name} at {payload.company}. "
        f"Pain points: {', '.join(payload.pain_points)}. "
        f"Value prop: {payload.product_value}."
    )
    return ai_service.generate(prompt, payload.model_dump())


@app.post("/leads/score")
def lead_score(payload: LeadScoringRequest) -> dict:
    return score_lead(payload).model_dump()


@app.post("/market/analysis")
def market_analysis(payload: MarketAnalysisRequest) -> dict:
    prompt = (
        f"Analyze market segment {payload.market_segment} in {payload.region}. "
        f"Competitors: {', '.join(payload.competitors) if payload.competitors else 'none listed'}."
    )
    return ai_service.generate(prompt, payload.model_dump())


@app.post("/business/insights")
def business_insights(payload: BusinessInsightsRequest) -> dict:
    return generate_business_insights(payload).model_dump()
