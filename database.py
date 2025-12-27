import json
import pyodbc

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._connect()
        return cls._instance

    def _connect(self):
        with open("config/db_config.json", "r") as file:
            config = json.load(file)

        connection_string = (
            f"DRIVER={config['driver']};"
            f"SERVER={config['server']};"
            f"DATABASE={config['database']};"
            f"UID={config['username']};"
            f"PWD={config['password']}"
        )

        self.connection = pyodbc.connect(connection_string)

    def get_connection(self):
        return self.connection