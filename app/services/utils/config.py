# app/services/utils/config.py

# Utilities for OpenAI configuration

import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "your_openai_api_key")
    mock_openai: bool = True

def load_config() -> Settings:
    """
    Load application configuration.
    """
    return Settings()

