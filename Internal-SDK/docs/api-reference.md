# API Reference: GatewayClient

## GatewayClient
Main class to interact with the internal API gateway.

### `__init__(base_url: str, token: str, retries: int = 3, timeout: int = 5)`
- `base_url`: Base URL of the API
- `token`: Bearer token for authorization
- `retries`: Number of retry attempts
- `timeout`: Request timeout in seconds

### `get(path: str) -> dict`
Sends a GET request to the API.

### `post(path: str, data: dict) -> dict`
Sends a POST request with JSON payload.

### `put(path: str, data: dict) -> dict`
Sends a PUT request with JSON payload.

### `delete(path: str) -> bool`
Sends a DELETE request to the API. Returns `True` if successful (HTTP 204).