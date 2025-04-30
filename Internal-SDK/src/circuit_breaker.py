import time
from src.exceptions import CircuitOpenError

class CircuitBreaker:
    def __init__(self, threshold=5, recovery_timeout=60):
        self.threshold = threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.open = False

    def call(self, func, *args, **kwargs):
        if self.open and time.time() - self.last_failure_time < self.recovery_timeout:
            raise CircuitOpenError("Circuit is open. Try again later.")
        try:
            result = func(*args, **kwargs)
            self.reset()
            return result
        except Exception:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.failure_count >= self.threshold:
                self.open = True
            raise

    def reset(self):
        self.failure_count = 0
        self.open = False