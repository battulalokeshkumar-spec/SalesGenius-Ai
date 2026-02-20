from statistics import mean
from .models import LeadScoringRequest, LeadScoreResponse, BusinessInsightsRequest, BusinessInsightResponse


def score_lead(payload: LeadScoringRequest) -> LeadScoreResponse:
    size_score = min(payload.company_size / 1000 * 10, 10)
    budget_score = min(payload.budget / 100000 * 10, 10)

    weighted = (
        size_score * 0.25
        + budget_score * 0.30
        + payload.engagement_level * 0.25
        + payload.industry_fit * 0.20
    )
    score = round(weighted * 10)

    if score >= 80:
        tier = "Hot"
    elif score >= 60:
        tier = "Warm"
    else:
        tier = "Cold"

    return LeadScoreResponse(
        score=score,
        tier=tier,
        rationale={
            "company_size": round(size_score, 2),
            "budget": round(budget_score, 2),
            "engagement_level": payload.engagement_level,
            "industry_fit": payload.industry_fit,
        },
    )


def generate_business_insights(payload: BusinessInsightsRequest) -> BusinessInsightResponse:
    if not payload.monthly_revenue or not payload.marketing_spend or not payload.conversion_rate:
        return BusinessInsightResponse(
            trend_summary="Insufficient data to build trends.",
            suggested_actions=["Provide at least 3 months of KPI data."],
        )

    revenue_growth = payload.monthly_revenue[-1] - payload.monthly_revenue[0]
    cpa = mean(payload.marketing_spend) / max(mean(payload.conversion_rate), 0.01)

    trend = (
        f"Revenue change across period: {revenue_growth:.2f}. "
        f"Estimated spend-to-conversion efficiency index: {cpa:.2f}."
    )

    actions = [
        "Double down on channels with highest conversion consistency.",
        "Run A/B testing on top-funnel creatives every 2 weeks.",
        "Align SDR outreach with segments showing conversion lift.",
    ]

    if revenue_growth < 0:
        actions.insert(0, "Prioritize retention campaigns and win-back sequences.")

    return BusinessInsightResponse(trend_summary=trend, suggested_actions=actions)
