from employee import Employee
from employee_dao import EmployeeDAO

def main():
    dao = EmployeeDAO()

    # Добавляем нового сотрудника
    employee1 = Employee(name="John Doe", position="Software Engineer", salary=75000.0, hire_date="2025-04-01")
    dao.insert(employee1)
    print("Inserted new employee.")

    # Получаем сотрудника по ID
    emp = dao.get_by_id(1)  # Получаем сотрудника с ID 1
    if emp:
        print(f"Employee Retrieved: {emp}")
    else:
        print("Employee not found!")

    # Получаем всех сотрудников
    employees = dao.get_all()
    print("All employees:")
    for emp in employees:
        print(emp)

    # Обновляем данные сотрудника
    if emp:
        emp.set_salary(80000.0)
        emp.set_position("Senior Software Engineer")
        dao.update(emp)
        print(f"Updated Employee: {emp}")

    # Удаляем сотрудника по ID
    dao.delete(1)
    print("Employee deleted.")

if __name__ == "__main__":
    main()
