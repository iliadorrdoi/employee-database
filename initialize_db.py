import sqlite3

def create_database():
    conn = sqlite3.connect('employee_db.db')
    cursor = conn.cursor()

    # Создание таблицы employees
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee (
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
    create_database()
