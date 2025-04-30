import requests
from requests.exceptions import RequestException
from src.config_loader import ConfigLoader
from src.logger import setup_logger
from src.utils import build_url
from src.circuit_breaker import CircuitBreaker
from src.exceptions import APIError

class GatewayClient:
    def __init__(self, config_path='configs/config.yaml'):
        config = ConfigLoader.load(config_path)
        api_cfg = config['api']

        self.base_url = api_cfg['base_url']
        self.token = api_cfg['token']
        self.retries = api_cfg.get('retries', 3)
        self.timeout = api_cfg.get('timeout', 5)
        self.logger = setup_logger(level=api_cfg.get('log_level', 'INFO'))
        self.verify_ssl = api_cfg.get('verify_ssl', True)

        cb_cfg = config.get('circuit_breaker', {})
        self.circuit_enabled = cb_cfg.get('enabled', False)
        self.circuit_breaker = CircuitBreaker(
            threshold=cb_cfg.get('failure_threshold', 5),
            recovery_timeout=cb_cfg.get('recovery_timeout', 60)
        ) if self.circuit_enabled else None

        self.session = requests.Session()

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def _request(self, method, path, **kwargs):
        url = build_url(self.base_url, path)
        for attempt in range(1, self.retries + 1):
            try:
                self.logger.debug(f"Attempt {attempt}: {method.upper()} {url}")
                response = self.session.request(
                    method=method,
                    url=url,
                    headers=self._headers(),
                    timeout=self.timeout,
                    verify=self.verify_ssl,
                    **kwargs
                )
                response.raise_for_status()
                return response.json() if response.content else {}
            except RequestException as e:
                self.logger.warning(f"{method.upper()} attempt {attempt} failed: {e}")
                if attempt == self.retries:
                    raise APIError(f"{method.upper()} request failed after {self.retries} attempts.")

    def get(self, path):
        if self.circuit_enabled:
            return self.circuit_breaker.call(self._request, 'get', path)
        return self._request('get', path)

    def post(self, path, data):
        if self.circuit_enabled:
            return self.circuit_breaker.call(self._request, 'post', path, json=data)
        return self._request('post', path, json=data)

    def put(self, path, data):
        if self.circuit_enabled:
            return self.circuit_breaker.call(self._request, 'put', path, json=data)
        return self._request('put', path, json=data)

    def delete(self, path):
        if self.circuit_enabled:
            return self.circuit_breaker.call(self._request, 'delete', path)
        return self._request('delete', path)
    
'''
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
'''
