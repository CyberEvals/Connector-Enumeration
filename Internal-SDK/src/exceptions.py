class APIError(Exception):
    pass

class AuthenticationError(APIError):
    pass

class RateLimitError(APIError):
    pass

class CircuitOpenError(APIError):
    pass
