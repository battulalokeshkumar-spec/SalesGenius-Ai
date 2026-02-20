# MarketMind: Generative AI-Powered Sales & Marketing Intelligence Platform

MarketMind is a full-stack starter platform for sales and marketing teams to generate campaigns, draft pitches, score leads, and produce actionable business insights.

## Core Capabilities
- Campaign generation
- Sales pitch creation
- Lead scoring
- Market analysis
- Business insights

## Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** React + JavaScript (Vite)
- **AI Provider Abstraction:** Gemini, IBM AI, Groq, Hugging Face (with local fallback template engine)

## Project Structure
- `backend/` FastAPI APIs and analytics logic
- `frontend/` React interface

## Backend Quickstart
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Frontend Quickstart
```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

## API Endpoints
- `POST /campaigns/generate`
- `POST /sales/pitch`
- `POST /leads/score`
- `POST /market/analysis`
- `POST /business/insights`
- `GET /health`

## Environment Variables (Optional)
If configured, the backend can route generation requests to specific LLM providers:
- `LLM_PROVIDER` (`Gemini`, `Groq`, `HuggingFace`, `IBM`)
- `GEMINI_API_KEY`
- `GROQ_API_KEY`
- `HUGGINGFACE_API_KEY`
- `IBM_API_KEY`

Without keys, the system uses a deterministic template engine for local development.
