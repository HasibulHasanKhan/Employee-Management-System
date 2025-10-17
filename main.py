from employee_crud import create_table, add_employee, view_employees, update_salary, delete_employee
import datetime

def menu():
    print("\n=== Employee Management System ===")
    print("1. Create Table")
    print("2. Add Employee")
    print("3. View Employees")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")
    return input("Enter your choice: ")

if __name__ == "__main__":
    while True:
        choice = menu()

        if choice == '1':
            create_table()
            print("Table created successfully!")

        elif choice == '2':
            name = input("Name: ")
            salary = float(input("Salary: "))
            department = input("Department: ")
            join_date = datetime.date.today()
            add_employee(name, salary, department, join_date)

        elif choice == '3':
            view_employees()

        elif choice == '4':
            emp_id = int(input("Employee ID to update: "))
            new_salary = float(input("New Salary: "))
            update_salary(emp_id, new_salary)

        elif choice == '5':
            emp_id = int(input("Employee ID to delete: "))
            delete_employee(emp_id)

        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
