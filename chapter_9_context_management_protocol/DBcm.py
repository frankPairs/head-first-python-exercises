import psycopg2


class UseDatabase:
    def __init__(self, db_config: dict) -> None:
        self.config = db_config

    def __enter__(self) -> 'cursor':
        self.conn = psycopg2.connect(**self.config)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        self.cursor.close()
