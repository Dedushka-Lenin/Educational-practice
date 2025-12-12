import sqlite3

from internal.adapter.repo.sql_queries import material_type_query

class MaterialTypeRepo:
    def __init__(self, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
        self.query = material_type_query()

        self.conn = conn
        self.cursor = cursor

    def create(self, material_type: str, raw_material_loss_percentage: str):
        values = (material_type, raw_material_loss_percentage)
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