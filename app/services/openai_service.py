# app/services/openai_service.py

# OpenAI Service Logic
from openai import OpenAI
from pydantic import Field
from app.services.utils.config import load_config
import logging

# Get logger instance
logger = logging.getLogger(__name__)

# Read configuration settings
settings = load_config()

skip: bool = settings.mock_openai
api_key: str = settings.openai_api_key
client: OpenAI = OpenAI(api_key=api_key)

async def generate_text(model: str, prompt: str) -> str:
    """
    Calls the OpenAI API to generate text.
    """
    try:
        logger.info(f"open_service.generate_text called with prompt: {prompt} using model: {model}")
        if skip:
            return "Skipped the call to openai"
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            stop="\n",
            max_tokens=256
        )
        logger.info(f"open_service.generate_text returned successfully.")
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"Error calling OpenAI API: {e}")
