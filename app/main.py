from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="FastAPI Demo",
    description="A simple FastAPI application",
    version="0.1.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Demo API"} 