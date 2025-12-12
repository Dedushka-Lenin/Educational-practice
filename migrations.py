import os
import sqlite3
import csv


folder_path = 'data/csv'
db_path = 'db/app.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        table_name = os.path.splitext(filename)[0]
        
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)  # читаем заголовки без 'id'
            
            # Создаём список колонок, добавляя 'id' как автоинкрементный первичный ключ
            columns = ['"id" INTEGER PRIMARY KEY AUTOINCREMENT']
            for header in headers:
                columns.append(f'"{header}" TEXT')
            columns_sql = ', '.join(columns)
            
            # Создаем таблицу
            create_table_sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns_sql});'
            cursor.execute(create_table_sql)
            
            # Вставляем данные без 'id' — он создастся автоматически
            for row in reader:
                columns_list = [f'"{h}"' for h in headers]
                columns_str = ', '.join(columns_list)
                placeholders = ', '.join(['?'] * len(row))
                insert_sql = f'INSERT INTO "{table_name}" ({columns_str}) VALUES ({placeholders});'
                cursor.execute(insert_sql, row)

conn.commit()
conn.close()

print("Импорт завершен.")