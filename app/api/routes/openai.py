# app/api/routes/openai.py

# OpenAI-related API routes
from fastapi import APIRouter, HTTPException
from app.models.schemas import GenerateRequest, GenerateResponse
from app.services.openai_service import generate_text
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    """
    Generate text using OpenAI's GPT model.
    """
    try:
        logger.info(f"Generating insight for prompt: {request.prompt} using model: {request.model}")
        result = await generate_text(request.model, request.prompt)
        return GenerateResponse(result=result)
    except ValueError as ve:
        logger.error(f"Invalid model specified: {request.model}. Error: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"Error generating insight: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating insight: {str(e)}")
