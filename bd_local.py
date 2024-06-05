import psycopg2
from singleton import SingletonMeta
class Bd_local(metaclass=SingletonMeta):
    """
    Represents a connection to the database.

    Attributes:
        conn (psycopg2.extensions.connection): The database connection object.
        cursor (psycopg2.extensions.cursor): The database cursor object.
    """

    def __init__(self) -> None:
        server = 'localhost'
        database = 'proyecto3'
        username = 'postgres'
        password = '4993'
        port = '5432'
        connection = psycopg2.connect(
            user=username,
            password=password,
            host=server,
            port=port,
            database=database
        )
        self.conn = connection
        self.cursor = self.conn.cursor()