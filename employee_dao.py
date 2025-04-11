import sqlite3
from employee import Employee

class EmployeeDAO:
    def __init__(self, db_name='employee_db.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def insert(self, employee: Employee):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO employee (name, position, salary, hire_date)
        VALUES (?, ?, ?, ?)
        ''', (employee.name, employee.position, employee.salary, employee.hire_date))
        conn.commit()
        conn.close()

    def get_by_id(self, id: int):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employee WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Employee(row[1], row[2], row[3], row[4], row[0])
        return None

    def get_all(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employee')
        rows = cursor.fetchall()
        conn.close()
        return [Employee(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    def update(self, employee: Employee):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE employee SET name = ?, position = ?, salary = ?, hire_date = ?
        WHERE id = ?
        ''', (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        conn.commit()
        conn.close()

    def delete(self, id: int):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM employee WHERE id = ?', (id,))
        conn.commit()
        conn.close()
