"""Configuration for MCP Video Generation Service."""

import os
from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Service Configuration
    SERVICE_NAME: str = Field(default="mcp-video-generation-service")
    ENVIRONMENT: str = Field(default="development")
    LOG_LEVEL: str = Field(default="INFO")

    # FAL.ai Configuration
    FAL_API_KEY: str = Field(..., description="FAL.ai API key")
    FAL_IMAGE_TO_VIDEO: str = Field(default="fal-ai/veo3/fast/image-to-video")
    FAL_TEXT_TO_VIDEO: str = Field(default="fal-ai/fast-sdxl")

    # OpenRouter LLM Configuration
    OPENROUTER_API_KEY: Optional[str] = Field(default=None)
    OPENROUTER_DEFAULT_MODEL: Optional[str] = Field(default=None)
    OPENROUTER_BACKUP_MODEL: Optional[str] = Field(default=None)
    OPENROUTER_BASE_URL: Optional[str] = Field(default=None)

    # PayloadCMS Integration
    PAYLOADCMS_API_URL: str = Field(default="http://localhost:3010")
    PAYLOADCMS_API_KEY: Optional[str] = Field(default=None)

    # Brain Service Configuration
    BRAIN_SERVICE_URL: str = Field(default="http://localhost:8002")
    BRAIN_SERVICE_WS_URL: str = Field(default="ws://localhost:8002/mcp")

    # Video Generation Settings
    DEFAULT_DURATION_PER_SEGMENT: float = Field(default=3.0)
    MAX_CONCURRENT_JOBS: int = Field(default=3)
    SYNTHESIS_TIMEOUT_SECONDS: int = Field(default=300)

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
