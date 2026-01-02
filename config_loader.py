import json
import os

class ConfigError(Exception):
    pass

class ConfigLoader:
    REQUIRED_DB_KEYS = {
        "server": str,
        "database": str,
        "username": str,
        "password": str,
        "driver": str
    }

    @staticmethod
    def load_config(path="db_config.json"):
        if not os.path.exists(path):
            raise ConfigError(f"Config file '{path}' not found")

        try:
            with open(path, "r", encoding="utf-8") as f:
                config = json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigError(f"Invalid JSON format: {e}")

        ConfigLoader._validate_config(config)
        return config

    @staticmethod
    def _validate_config(config):
        if "db" not in config:
            raise ConfigError("Missing 'db' section in config file")

        db = config["db"]

        for key, expected_type in ConfigLoader.REQUIRED_DB_KEYS.items():
            if key not in db:
                raise ConfigError(f"Missing database config key: '{key}'")

            value = db[key]

            if not isinstance(value, expected_type):
                raise ConfigError(f"Invalid type for '{key}': expected type is {expected_type.__name__}")

            if isinstance(value, str) and not value.strip():
                raise ConfigError(f"Config value '{key}' must not be empty")