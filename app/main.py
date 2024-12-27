# app/main.py

# Entry point for the application
from fastapi import FastAPI
from app.api.routes.openai import router as openai_router
from app.services.utils.config import load_config
from app.services.utils.logging import setup_logging

# Load configurations
config = load_config()

# Set up logging for the application
setup_logging(log_level="DEBUG", log_file="logs/vitaledge_analytics.log")

app = FastAPI(title="VitalEdge Open LLM")

# Include OpenAI-related routes
app.include_router(openai_router, prefix="/openai", tags=["OpenAI"])

@app.get("/")
async def root():
    return {"message": "Welcome to VitalEdge Open LLM API"}



# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import openai
# import os

# app = FastAPI(title="VitalEdge OpenAI LLM Microservice")

# # OpenAI API Key
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Request and Response Schemas
# class PromptRequest(BaseModel):
#     prompt: str

# class EmbeddingRequest(BaseModel):
#     texts: list[str]

# @app.get("/health")
# def health_check():
#     return {"status": "ok"}

# @app.post("/generate")
# def generate_text(request: PromptRequest):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4o",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": request.prompt},
#             ]
#         )
#         result = response["choices"][0]["message"]["content"]
#         return {"response": result}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/embed")
# def generate_embeddings(request: EmbeddingRequest):
#     try:
#         response = openai.Embedding.create(
#             model="text-embedding-3-small",
#             input=request.texts
#         )
#         embeddings = [item["embedding"] for item in response["data"]]
#         return {"embeddings": embeddings}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/models")
# def list_models():
#     return {"models": ["gpt-4o", "gpt-3.5-turbo", "text-embedding-3-small"]}
