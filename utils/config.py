import json
import os

def load_config():
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'data.json')
    with open(config_path, 'r') as f:
        return json.load(f)
