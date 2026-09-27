from fastapi import FastAPI
from routes import router

app = FastAPI(title="LegalEase API", version="1.0.0")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "LegalEase API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
