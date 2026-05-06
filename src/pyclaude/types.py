"""Type definitions for pyclaude."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class MessageResponse(BaseModel):
    """Response from a Claude message."""

    content: str
    model: str
    role: str
    stop_reason: str
    usage: dict[str, int]

    @classmethod
    def from_anthropic(cls, response: Any) -> MessageResponse:
        """Create MessageResponse from Anthropic API response.

        Args:
            response: Raw Anthropic API response.

        Returns:
            Parsed MessageResponse.
        """
        content = response.content[0].text if response.content else ""
        return cls(
            content=content,
            model=response.model,
            role=response.role,
            stop_reason=response.stop_reason,
            usage={
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
            },
        )