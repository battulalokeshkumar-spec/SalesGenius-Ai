from app.analytics import score_lead, generate_business_insights
from app.models import LeadScoringRequest, BusinessInsightsRequest


def test_score_lead_hot_tier():
    payload = LeadScoringRequest(
        company_size=1200,
        budget=150000,
        engagement_level=9,
        industry_fit=8,
    )
    result = score_lead(payload)
    assert result.tier == "Hot"
    assert result.score >= 80


def test_business_insights_output():
    payload = BusinessInsightsRequest(
        monthly_revenue=[10000, 12000, 15000],
        marketing_spend=[3000, 3500, 3800],
        conversion_rate=[2.0, 2.5, 2.8],
    )
    result = generate_business_insights(payload)
    assert "Revenue change" in result.trend_summary
    assert len(result.suggested_actions) >= 3
