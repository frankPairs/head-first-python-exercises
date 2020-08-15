import psycopg2


class ConnectionDBError(Exception):
    pass


class SQLError(Exception):
    pass


class UseDatabase:
    def __init__(self, db_config: dict) -> None:
        self.config = db_config

    def __enter__(self) -> 'cursor':
        try:
            self.conn = psycopg2.connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except psycopg2.OperationalError as err:
            print('DB connection error: ' + str(err))
            raise ConnectionDBError(err)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        self.cursor.close()

        print(exc_type)
        if exc_type is psycopg2.errors.SyntaxError:
            raise SQLError(exc_val)
        elif exc_type:
            raise exc_type(exc_val)
