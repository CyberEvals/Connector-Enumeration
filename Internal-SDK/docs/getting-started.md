# Getting Started

## Prerequisites
- Python 3.8+
- pip (Python package installer)

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Create a `.env` file or use the `configs/config.yaml` file to store API configuration:
```yaml
api:
  base_url: https://api.example.com
  retries: 3
  timeout: 5
```

## Example Usage
```python
from src.gateway_client import GatewayClient

client = GatewayClient(base_url="https://api.example.com", token="your-token")
data = client.get("status")
print(data)
```