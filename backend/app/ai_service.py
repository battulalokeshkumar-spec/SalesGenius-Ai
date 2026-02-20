import os
from typing import Dict, Any


class AIProviderService:
    """Simple provider router for LLM-backed generation with safe fallback behavior."""

    def __init__(self) -> None:
        self.default_provider = os.getenv("LLM_PROVIDER", "Gemini")
        self.available = {
            "Gemini": bool(os.getenv("GEMINI_API_KEY")),
            "Groq": bool(os.getenv("GROQ_API_KEY")),
            "HuggingFace": bool(os.getenv("HUGGINGFACE_API_KEY")),
            "IBM": bool(os.getenv("IBM_API_KEY")),
        }

    def generate(self, prompt: str, metadata: Dict[str, Any] | None = None) -> Dict[str, str]:
        provider = self.default_provider
        if not self.available.get(provider, False):
            provider = "TemplateEngine"

        if provider == "TemplateEngine":
            return {
                "provider": provider,
                "content": self._template_response(prompt, metadata or {}),
            }

        # Placeholder for real provider calls; kept deterministic for local development.
        return {
            "provider": provider,
            "content": f"[{provider}] Generated output for: {prompt}",
        }

    def _template_response(self, prompt: str, metadata: Dict[str, Any]) -> str:
        context = ", ".join(f"{k}: {v}" for k, v in metadata.items())
        return (
            "AI provider keys were not configured. Here's a strategic draft based on your request.\n"
            f"Prompt: {prompt}\n"
            f"Context: {context if context else 'N/A'}\n"
            "Recommendation: Focus on a clear ICP, high-intent channel testing, and measurable funnel KPIs."
        )
