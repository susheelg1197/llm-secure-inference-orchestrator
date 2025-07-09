from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import time
import logging
import os

app = FastAPI()
logger = logging.getLogger("uvicorn")

class InferenceRequest(BaseModel):
    prompt: str
    tenant_id: str
    api_key: str

@app.post("/infer")
async def infer(request: InferenceRequest):
    start_time = time.time()
    logger.info(f"Received request from tenant: {request.tenant_id}")

    if request.api_key != "secure_dummy_key":
        raise HTTPException(status_code=403, detail="Invalid API Key")

    explanation = f"This is a placeholder explanation for: {request.prompt}"
    duration = time.time() - start_time

    logger.info(f"Tenant: {request.tenant_id}, Time: {duration:.2f}s")
    return {
        "tenant_id": request.tenant_id,
        "response": explanation,
        "latency": duration
    }