import sqlite3

from internal.adapter.repo.sql_queries import users_query


class UsersRepo:
    def __init__(self, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
        self.query = users_query()

        self.conn = conn
        self.cursor = cursor

    def create(self, fio: str, phone: int, login: str, password: str, type: str):
        values = (fio, phone, login, password, type)
        self.cursor.execute(self.query.create, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def get(self, item_id) -> dict:
        self.cursor.execute(
            self.query.get,
            (item_id,)
        )
        return self.cursor.fetchone()
    
    def get_for_login(self, login) -> dict:
        self.cursor.execute(
            self.query.get_for_login,
            (login,)
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
    
    def check_login(self, login):
        self.cursor.execute(
            self.query.check_login,
            (login,)
        )
        return self.cursor.fetchone() is not None

    def delete(self, item_id):
        self.cursor.execute(
            self.query.delete,
            (item_id,)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0