import sqlite3

from internal.adapter.repo.sql_queries import token_query


class TokenRepo:
    def __init__(self, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
        self.query = token_query()

        self.conn = conn
        self.cursor = cursor
    def create(self, user_id: int, token: str):
        values = (user_id, token)
        self.cursor.execute(self.query.create, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def get(self, item_id):
        self.cursor.execute(
            self.query.get,
            (item_id,)
        )
        return self.cursor.fetchone()

    def check(self, token):
        self.cursor.execute(
            self.query.check,
            (token,)
        )
        return self.cursor.fetchone() is not None

    def delete(self, token):
        self.cursor.execute(
            self.query.delete,
            (token,)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0