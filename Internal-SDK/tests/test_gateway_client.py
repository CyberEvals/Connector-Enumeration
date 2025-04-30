# ghp_faK3T0k3n1234567890AbCdEfGhIjKlMnOpQrStUv
import unittest
from unittest.mock import patch, MagicMock
from src.gateway_client import GatewayClient

class TestGatewayClient(unittest.TestCase):
    def setUp(self):
        self.client = GatewayClient(base_url="https://api.example.com", token="testtoken", retries=1)

    @patch("src.gateway_client.requests.Session.get")
    def test_get_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response

        result = self.client.get("/test")
        self.assertEqual(result, {"key": "value"})

    @patch("src.gateway_client.requests.Session.post")
    def test_post_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        result = self.client.post("/submit", {"data": 123})
        self.assertEqual(result, {"success": True})

if __name__ == "__main__":
    unittest.main()