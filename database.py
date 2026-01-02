import pyodbc
from config_loader import ConfigLoader, ConfigError

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = None
            cls._instance._connect()
        return cls._instance

    def _connect(self):
        try:
            config = ConfigLoader.load_config()

            connection_string = (
                f"DRIVER={{{config['driver']}}};"
                f"SERVER={config['server']};"
                f"DATABASE={config['database']};"
                f"UID={config['username']};"
                f"PWD={config['password']}"
            )

            self.connection = pyodbc.connect(connection_string)

        except ConfigError as ce:
            raise RuntimeError(f"Configuration Error: {ce}")
        except pyodbc.Error as e:
            raise RuntimeError(f"Database connection failed: {e}")

    def get_connection(self):
        return self.connection