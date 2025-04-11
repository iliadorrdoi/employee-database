from employee import Employee
from employee_dao import EmployeeDAO

def main():
    dao = EmployeeDAO()

    # Вставляем нового сотрудника
    employee1 = Employee(name="John Doe", position="Software Engineer", salary=75000.0, hire_date="2025-04-01")
    dao.insert(employee1)
    print("Inserted new employee.")

    # Получаем ID последнего добавленного сотрудника
    # Мы можем воспользоваться методом get_all() для получения всех сотрудников.
    employees = dao.get_all()
    if employees:
        print(f"Inserted Employee ID: {employees[-1].get_id()}")  # Выводим ID последнего добавленного сотрудника
    
    # Попытка получить сотрудника по ID 1
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
    if employees:
        emp = employees[-1]  # Предполагаем, что обновляем последнего добавленного сотрудника
        emp.set_salary(80000.0)
        emp.set_position("Senior Software Engineer")
        dao.update(emp)
        print(f"Updated Employee: {emp}")

    # Удаляем сотрудника по ID
    if employees:
        dao.delete(employees[-1].get_id())
        print("Employee deleted.")

if __name__ == "__main__":
    main()
