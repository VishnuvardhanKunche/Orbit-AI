from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import uvicorn
import asyncio

from models import TripRequest, TripResponse, ChatRequest, ChatResponse
from agent import TripAgent


# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Orbit AI Backend Ready [OK] -- DEMO MODE")
    yield


# App
app = FastAPI(title="Orbit AI Backend", version="1.0", lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)


@app.get("/health")
def health_check():
    return {"status": "ok", "mode": "demo", "version": "1.0"}


@app.post("/plan-trip")
async def plan_trip(req: TripRequest):
    agent = TripAgent()
    try:
        result = agent.plan_trip(req)
        return result
    except Exception as e:
        print(f"plan_trip error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat")
async def chat(req: ChatRequest):
    agent = TripAgent()
    try:
        result = agent.chat(req)
        return result
    except Exception as e:
        print(f"chat error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)