import sqlite3
from contextlib import contextmanager
from typing import Iterator

class DatabaseConnection:
    def __init__(
            self, db_type: str = 'sqlite3', db_file: str= 'data/vehiculos.db'
) -> None:
        """
        Class for connecting to a database.

        Args: 
            db_type(str, optional): Database type.
                Defaults to 'sqlite3'.
            db_file(str, optional): Database file.
                Defaults to 'data/vehiculos.db'.
        """
        self.__db_type = db_type
        self.__db_file = db_file

    def get_connection(self) -> sqlite3.Connection:
        """
        Managed database connection.

        Return:
            sqlite3.Cursor: A sqlite3 connection.
        """
        if self.__db_type == 'sqlite3':
            _conn = sqlite3.connect(self.__db_file)
            return _conn
    
    def __str__(self) -> str:
        return f'{self.__db_type}://{self.__db_file}'