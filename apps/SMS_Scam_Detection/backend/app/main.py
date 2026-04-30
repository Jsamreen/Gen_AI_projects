from fastapi import FastAPI
from app.routes.scam import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "SMS Scam Detection API is running successfully"}