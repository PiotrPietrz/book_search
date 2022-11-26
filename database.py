import sqlite3
import pandas as pd
from typing import List, Tuple


class DataBase:
    """
    Class for managing sqlite3 database
    """

    def connect(self) -> sqlite3.Connection:
        """
        Function for creating a connection to the database.
        Returns sqlite3 connection
        """
        path = "warehouse/storage.db"
        con = sqlite3.connect(path)

        return con

    def query_db(self, query: str) -> List[Tuple]:
        """
        Function for processing a db query. Returns a list of tuples.
        """
        con = self.connect()
        cur = con.cursor()

        try:
            cur.execute(query)
            res = cur.fetchall()
            con.commit()
            con.close()
            return res
        except:
            raise Exception("Unable to execute the query.")

    def to_df(self, query) -> pd.DataFrame:
        """
        Method for getting a DataFrame based on the query.
        """
        return pd.read_sql(sql=query, con=self.connect())

    def table_exists(self, table_name: str) -> bool:
        """
        Checks if a table is already in the database.
        Returns boolean
        """

        query = f"""
                SELECT * FROM sqlite_master
                WHERE type='table' AND name='{table_name}'
                ORDER BY name;
                """

        res = self.query_db(query)

        if len(res) == 0:
            return False
        else:
            return True

    @classmethod
    def create_backup(cls):
        pass
