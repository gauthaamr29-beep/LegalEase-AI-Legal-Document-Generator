# LegalEase — AI-Powered Legal Document Generator

This starter project follows the uploaded LegalEase specification: Streamlit frontend, FastAPI backend, Gemini-based generation, editable preview, and TXT/DOCX/PDF export.

## Setup

1. Create a virtual environment:
   `python -m venv .venv`
2. Activate it.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your Gemini API key.
5. Start the backend:
   `uvicorn main:app --reload`
6. In another terminal start the frontend:
   `streamlit run app.py`

The generated document can be edited and downloaded as TXT, DOCX, or PDF.

This is an educational project and does not replace professional legal advice.
