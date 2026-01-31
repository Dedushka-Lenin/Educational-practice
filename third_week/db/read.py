import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('db/app.db')
cursor = conn.cursor()

# Получение списка всех таблиц
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table_name_tuple in tables:
    table_name = table_name_tuple[0]
    print(f"Таблица: {table_name}")

    # Получение информации о столбцах
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()  # Каждое значение: (cid, name, type, notnull, dflt_value, pk)

    print("Поля и типы:")
    for col in columns:
        col_name = col[1]
        col_type = col[2]
        print(f" - {col_name}: {col_type}")

    print("\nДанные таблицы:")
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        if rows:
            # Выводим заголовки
            column_names = [col[1] for col in columns]
            print(" | ".join(column_names))
            print("-" * 50)
            # Вывод строк
            for row in rows:
                print(" | ".join(str(item) for item in row))
        else:
            print("Нет данных")
    except sqlite3.Error as e:
        print(f"Ошибка при чтении таблицы {table_name}: {e}")

    print("\n" + "="*80 + "\n")

# Закрытие соединения
conn.close()