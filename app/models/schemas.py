# app/models/schemas.py

# Pydantic Models for API requests and responses
from pydantic import BaseModel

class GenerateRequest(BaseModel):
    prompt: str
    model: str

class GenerateResponse(BaseModel):
    result: str
