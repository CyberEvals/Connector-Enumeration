# Internal API Gateway SDK

A secure, retry-capable SDK for interacting with internal API gateways.

## Features
- Token-based authentication
- Retry logic with logging
- Extensible for additional API methods (PUT, DELETE)

## Getting Started
```bash
pip install -r requirements.txt
python src/main.py
```

## Environment Variables
- `API_BASE_URL` - Base URL of the API
- `API_TOKEN` - Auth token to access the API

## Usage
```python
from src.gateway_client import GatewayClient

client = GatewayClient(base_url="https://api.example.com", token="your-token")
data = client.get("/status")
print(data)
```
```

# CONTRIBUTING.md
```markdown
# Contributing Guide

Thanks for your interest in contributing! Please:
1. Fork this repo and create a feature branch
2. Follow existing code style and naming conventions
3. Submit a pull request with a clear description of the change
```

# CODE_OF_CONDUCT.md
```markdown
# Code of Conduct

All contributors are expected to uphold a respectful, inclusive environment.
Violations may result in moderation or bans from the project.
```

# SECURITY.md
```markdown
# Security Policy

If you discover a vulnerability, please report it responsibly to the maintainers.
Do not open public issues for security problems.
```

# CHANGELOG.md
```markdown
# Changelog

## [1.0.0] - Initial Release
- Implemented GatewayClient with GET, POST, PUT, DELETE
- Added basic test suite
- Added CI workflow