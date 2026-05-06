# pyclaude

Python library for Claude API interactions.

## Project Structure

```
src/pyclaude/
├── __init__.py      # Public API exports
├── client.py        # Main client implementation
├── types.py         # Pydantic models for requests/responses
└── conversation.py  # Conversation management
```

## Development Commands

- Run tests: `pytest`
- Type check: `mypy src/pyclaude`
- Lint: `ruff check src/pyclaude`
- Format: `ruff format src/pyclaude`

## Code Style

- Line length: 100 characters
- Use type hints everywhere
- Prefer composition over inheritance
- Use Pydantic models for data validation