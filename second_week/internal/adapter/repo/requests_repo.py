import sqlite3

from internal.adapter.repo.sql_queries import products_query

class ProductsRepo:
    def __init__(self, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
        self.query = products_query()

        self.conn = conn
        self.cursor = cursor

    def create(self, product_type: str, product_name: str, part_number: str, minimum_partner_cost: str, primary_material: str):
        values = (product_type, product_name, part_number, minimum_partner_cost, primary_material)
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