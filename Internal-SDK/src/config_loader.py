import os
import yaml

class ConfigLoader:
    @staticmethod
    def load(path='configs/config.yaml'):
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
        # Override with environment variables if they exist
        config['api']['base_url'] = os.getenv('API_BASE_URL', config['api']['base_url'])
        config['api']['token'] = os.getenv('API_TOKEN', config['api']['token'])
        return config