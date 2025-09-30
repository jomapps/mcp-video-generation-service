"""Configuration settings for MCP Video Generation Service."""

import os
from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Service Configuration
    SERVICE_NAME: str = Field(default="mcp-video-generation-service", description="Service name")
    ENVIRONMENT: str = Field(default="development", description="Deployment environment")
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")

    # FAL.ai Configuration
    FAL_API_KEY: str = Field(..., description="FAL.ai API key for video generation")
    FAL_IMAGE_TO_VIDEO: str = Field(
        default="fal-ai/veo3/fast/image-to-video",
        description="FAL.ai model for image-to-video synthesis"
    )
    FAL_TEXT_TO_VIDEO: str = Field(
        default="fal-ai/fast-sdxl",
        description="FAL.ai model for text-to-video synthesis"
    )
    FAL_TEXT_TO_IMAGE_MODEL: str = Field(
        default="fal-ai/flux/schnell",
        description="FAL.ai model for text-to-image"
    )
    FAL_IMAGE_TO_IMAGE_MODEL: str = Field(
        default="fal-ai/flux/dev",
        description="FAL.ai model for image-to-image"
    )

    # Video Generation Settings
    DEFAULT_DURATION_PER_SEGMENT: float = Field(
        default=3.0,
        description="Default duration per video segment in seconds"
    )
    DEFAULT_MOTION_STRENGTH: float = Field(
        default=0.6,
        description="Default motion strength for video synthesis"
    )
    MAX_TOTAL_RUNTIME: float = Field(
        default=12.0,
        description="Maximum total runtime for all segments"
    )
    DEFAULT_CHUNK_SIZE: int = Field(
        default=2,
        description="Default number of frames per video segment"
    )

    # OpenRouter LLM Configuration
    OPENROUTER_API_KEY: Optional[str] = Field(
        default=None,
        description="OpenRouter API key for LLM text processing"
    )
    OPENROUTER_DEFAULT_MODEL: Optional[str] = Field(
        default=None,
        description="Default OpenRouter model"
    )
    OPENROUTER_BACKUP_MODEL: Optional[str] = Field(
        default=None,
        description="Backup OpenRouter model"
    )
    OPENROUTER_BASE_URL: Optional[str] = Field(
        default=None,
        description="OpenRouter API base URL"
    )

    # ElevenLabs Configuration (Reserved)
    ELEVENLABS_API_KEY: Optional[str] = Field(
        default=None,
        description="ElevenLabs API key for voiceover workflows"
    )

    # PayloadCMS Integration
    PAYLOADCMS_API_URL: str = Field(
        default="http://localhost:3010",
        description="PayloadCMS API URL for asset storage"
    )
    PAYLOADCMS_API_KEY: Optional[str] = Field(
        default=None,
        description="PayloadCMS API key"
    )

    # Brain Service Configuration
    BRAIN_SERVICE_URL: str = Field(
        default="http://localhost:8002",
        description="MCP Brain Service URL"
    )
    BRAIN_SERVICE_WS_URL: str = Field(
        default="ws://localhost:8002/mcp",
        description="Brain Service WebSocket URL"
    )

    # Performance Settings
    MAX_CONCURRENT_JOBS: int = Field(
        default=3,
        description="Maximum concurrent video synthesis jobs"
    )
    SYNTHESIS_TIMEOUT_SECONDS: int = Field(
        default=300,
        description="Timeout for video synthesis in seconds"
    )
    WEBHOOK_ENABLED: bool = Field(
        default=False,
        description="Enable webhook support for long-running jobs"
    )

    # Monitoring
    ENABLE_METRICS: bool = Field(
        default=True,
        description="Enable Prometheus metrics"
    )
    METRICS_PORT: int = Field(
        default=9016,
        description="Prometheus metrics port"
    )

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
