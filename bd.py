import oracledb
from singleton import SingletonMeta

class Bd(metaclass=SingletonMeta):
    """
    Represents a connection to the database.

    Attributes:
        conn (cx_Oracle.Connection): The database connection object.
        cursor (cx_Oracle.Cursor): The database cursor object.
    """

    def __init__(self) -> None:
        self.user = "ADMIN"
        self.password = "A2laFU5aNqYN"

        # Configuración de la conexión
        self.connection = oracledb.connect(
            config_dir=r"C:\Users\leine\Downloads\Wallet_M55IVQWR5HLQRD1E",  # Directorio donde están los archivos tnsnames.ora y ewallet.pem
            user=self.user,
            password=self.password,
            dsn="m55ivqwr5hlqrd1e_high",  # Puedes cambiar a _high o _medium según lo necesites
            wallet_location=r"C:\Users\leine\Downloads\Wallet_M55IVQWR5HLQRD1E",  # El mismo directorio que config_dir
            wallet_password = "A2laFU5aNqYN"
        )
        self.cursor = self.connection.cursor()
        