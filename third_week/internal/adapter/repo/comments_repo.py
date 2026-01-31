import sqlite3

from internal.adapter.repo.sql_queries import comments_query

class CommentsRepo:
    def __init__(self, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
        self.query = comments_query()

        self.conn = conn
        self.cursor = cursor

    def create(self, message: str, masterID: int, requestID: int):
        values = (message, masterID, requestID)
        self.cursor.execute(self.query.create, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def get(self, item_id):
        self.cursor.execute(
            self.query.get,
            (item_id,)
        )
        return self.cursor.fetchone()

    def get_list(self):
        self.cursor.execute(self.query.get_list)
        result = [dict(row) for row in self.cursor.fetchall()]
        return result

    def check(self, item_id):
        self.cursor.execute(
            self.query.check,
            (item_id,)
        )
        return self.cursor.fetchone() is not None

    def delete(self, item_id):
        self.cursor.execute(
            self.query.delete,
            (item_id,)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0