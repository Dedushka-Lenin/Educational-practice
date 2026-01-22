import os
import sqlite3
import pandas as pd

folder_path = "data"
db_path = 'db/app.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        filepath = os.path.join(folder_path, filename)
        table_name = os.path.splitext(filename)[0]
        
        df = pd.read_csv(filepath)
        
        # Просто вставляем данные, таблица уже существует
        df.to_sql(table_name, conn, if_exists='append', index=False)
        print(f'Данные из файла {filename} добавлены в таблицу {table_name}')

conn.commit()
conn.close()