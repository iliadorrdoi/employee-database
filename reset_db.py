import sqlite3

def reset_database():
    conn = sqlite3.connect('employee_db.db')
    cursor = conn.cursor()

    # Удаляем таблицу (если она существует)
    cursor.execute('DROP TABLE IF EXISTS employee')
    
    # Пересоздаем таблицу
    cursor.execute('''
    CREATE TABLE employee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary REAL NOT NULL,
        hire_date TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    reset_database()
