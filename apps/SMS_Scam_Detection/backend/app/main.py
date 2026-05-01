from fastapi import FastAPI
from app.routes.scam import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "SMS Scam Detection API is running successfully"}