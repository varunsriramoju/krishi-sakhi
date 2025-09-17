# Krishi Sakhi - AI Personal Farming Assistant (Starter)

This is a starter full-stack project scaffold for **Krishi Sakhi** with multilingual features (Malayalam + English).
It includes a React frontend and FastAPI backend with basic endpoints for profiling, activity logging, and an advisory demo.

## Quick start (local)
- Backend:
  ```bash
  cd backend
  python -m venv .venv
  source .venv/bin/activate     # (Linux/macOS) or .venv\Scripts\activate (Windows)
  pip install -r requirements.txt
  uvicorn main:app --reload --port 8000
  ```
- Frontend (requires Node.js >=16):
  ```bash
  cd frontend
  npm install
  npm run dev
  ```
## Notes
- The translator and advisory engine are implemented to be functional: they attempt to use the OpenAI API if `OPENAI_API_KEY` is set as an env var. If not provided, the translator falls back to simple passthrough and advisory uses rule-based responses.
- This scaffold is intended to be expanded. Follow the code comments to plug in real datasets and APIs.
