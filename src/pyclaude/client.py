"""Main client for Claude API interactions."""

from anthropic import Anthropic

from pyclaude.types import MessageResponse


class Client:
    """Client for interacting with Claude API."""

    def __init__(self, api_key: str | None = None) -> None:
        """Initialize the Claude client.

        Args:
            api_key: Anthropic API key. If not provided, uses ANTHROPIC_API_KEY env var.
        """
        self._client = Anthropic(api_key=api_key)

    def chat(
        self,
        message: str,
        model: str = "claude-sonnet-4-6",
        max_tokens: int = 1024,
    ) -> MessageResponse:
        """Send a chat message to Claude.

        Args:
            message: The message to send.
            model: Claude model to use.
            max_tokens: Maximum tokens in response.

        Returns:
            The response from Claude.
        """
        response = self._client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": message}],
        )
        return MessageResponse.from_anthropic(response)