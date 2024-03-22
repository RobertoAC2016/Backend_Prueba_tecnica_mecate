import mysql.connector
from const import MYSQL_CONN

class MySQLConnection:

    def __init__(self, config=None):
        self.__new_conn(config or MYSQL_CONN)

    def __new_conn(self, config):
        self.cnx = mysql.connector.connect(**config, buffered=True)
        return self.cnx

    def newCommand(self, multi=False):
        """Nuevo comando"""
        return MySQLCommand(self.cnx, multi)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.cnx.close()


class MySQLCommand:

    def __init__(self, cnx, multi: bool):
        self.multi = multi
        self.Command = ""
        self.Params = None
        self.cursor = cnx.cursor(dictionary=True, buffered=True)

    def __enter__(self):
        return self

    def execute_non_query(self):
        self.execute()

    def execute(self):
        self.cursor.execute(self.Command, self.Params, multi=self.multi)
        return self.cursor

    def executemany(self):
        self.cursor.executemany(self.Command, self.Params)

    def __exit__(self, type, value, tb):
        self.cursor.close()