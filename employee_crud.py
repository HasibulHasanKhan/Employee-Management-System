from db_config import create_connection
import pandas as pd

def create_table():
    connection = create_connection()
    if not connection:
        print("❌ Connection failed")
        return
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        salary FLOAT,
        department VARCHAR(50),
        join_date DATE
    )
    """)
    connection.commit()
    cursor.close()
    connection.close()
    print("✅ Table created!")

def add_employee(name, salary, department, join_date):
    connection = create_connection()
    if not connection:
        print("❌ Connection failed")
        return
    cursor = connection.cursor()
    sql = "INSERT INTO employees (name, salary, department, join_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, salary, department, join_date))
    connection.commit()
    print(f"✅ Added {name} with ID {cursor.lastrowid}")
    cursor.close()
    connection.close()

def view_employees():
    connection = create_connection()
    if not connection:
        print("❌ Connection failed")
        return
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
    print(df)
    cursor.close()
    connection.close()

def update_salary(employee_id, new_salary):
    connection = create_connection()
    if not connection:
        print("❌ Connection failed")
        return
    cursor = connection.cursor()
    cursor.execute("UPDATE employees SET salary = %s WHERE id = %s", (new_salary, employee_id))
    connection.commit()
    print(f"✅ Salary updated for ID {employee_id}")
    cursor.close()
    connection.close()

def delete_employee(employee_id):
    connection = create_connection()
    if not connection:
        print("❌ Connection failed")
        return
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
    connection.commit()
    print(f"🗑️ Employee ID {employee_id} deleted")
    cursor.close()
    connection.close()
