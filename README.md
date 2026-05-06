# pyclaude

A Python library for building AI-powered applications with Claude.

## Installation

```bash
pip install pyclaude
```

## Quick Start

```python
from pyclaude import Client

client = Client()
response = client.chat("Hello, Claude!")
print(response)
```

## Features

- Simple, intuitive API for Claude interactions
- Built-in conversation management
- Type-safe with full Pydantic support
- Async-first design

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Type checking
mypy src/pyclaude

# Linting
ruff check src/pyclaude
```

## License

MIT