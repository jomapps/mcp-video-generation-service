from __future__ import annotations

import os
from typing import Optional, Dict, Any


class FalAIVideoClient:
    """
    Minimal FAL.ai image-to-video client (stub for MVP/testing).

    Notes:
    - Real implementation should call FAL.ai API endpoints with proper auth
      and payloads (primary/secondary image URLs, prompt, duration, etc.).
    - Webhook registration and polling should be handled by an orchestrator
      or dedicated async worker. This stub returns a mock URL for now.
    """

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("FAL_API_KEY")
        self.model = model or os.getenv("FAL_IMAGE_TO_VIDEO", "fal-ai/veo3/fast/image-to-video")

    async def synthesize(
        self,
        *,
        primary_image_url: str,
        secondary_image_url: Optional[str] = None,
        prompt: str,
        duration_seconds: float = 3.0,
        motion_strength: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Synthesize a video clip from 1-2 keyframes and a prompt.

        Returns a dict with keys: video_url, provider_metadata
        """
        # TODO: Replace with real network call to FAL.ai
        return {
            "video_url": "https://example.com/mock/segment.mp4",
            "provider_metadata": {
                "provider": "fal-ai",
                "model": self.model,
                "job_id": "mock-job",
                "webhook_id": None,
            },
        }

