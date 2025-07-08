# employee_crud_mysql1.py

import pymysql

def connect_db():
    try:
        connection = pymysql.Connect(
            host='localhost',
            user='root',
            password='root',
            database='samsung1',
            port=3306,
            charset='utf8'
        )
        print('Database Connected')
        return connection
    except pymysql.MySQLError as e:
        print(f'Database Connection Failed: {e}')
        return None

def disconnect_db(connection):
    try:
        connection.close()
        print('DB disconnected')
    except pymysql.MySQLError as e:
        print(f'DB disconnection failed: {e}')

def create_db():
    try:
        connection = pymysql.Connect(
            host='localhost',
            user='root',
            password='root123',
            port=3306,
            charset='utf8'
        )
        query = 'CREATE DATABASE IF NOT EXISTS nithin_db'
        cursor = connection.cursor()
        cursor.execute(query)
        print('Database created or already exists')
        cursor.close()
        disconnect_db(connection)
    except pymysql.MySQLError as e:
        print(f'Database creation failed: {e}')

def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS employee (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        designation VARCHAR(30),
        phone_number BIGINT UNIQUE,
        salary FLOAT,
        commission FLOAT DEFAULT 0,
        years_of_experience TINYINT,
        technology VARCHAR(30) NOT NULL
    )
    '''
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            print('Table created or already exists')
            cursor.close()
        except pymysql.MySQLError as e:
            print(f'Table creation failed: {e}')
        finally:
            disconnect_db(connection)

def read_all_employees():
    query = 'SELECT * FROM employee'
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            if not rows:
                print("No records found.")
            for row in rows:
                print(row)
            cursor.close()
        except pymysql.MySQLError as e:
            print(f'Row retrieval failed: {e}')
        finally:
            disconnect_db(connection)

def search_employee():
    emp_id = int(input('Enter Id of the employee to search: '))
    query = 'SELECT * FROM employee WHERE id = %s'
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query, (emp_id,))
            rows = cursor.fetchall()
            if not rows:
                print(f"No employee found with id = {emp_id}")
            for row in rows:
                print(row)
            cursor.close()
        except pymysql.MySQLError as e:
            print(f'Row retrieval failed: {e}')
        finally:
            disconnect_db(connection)

def read_employee_details():
    name = input('Enter employee name: ')
    designation = input('Enter employee designation: ')
    phone_number = int(input('Enter employee phone number: '))
    salary = float(input('Enter employee salary: '))
    commission = float(input('Enter employee commission: '))
    years_of_experience = int(input('Enter employee years of experience: '))
    technology = input('Enter employee technology: ')
    return (name, designation, phone_number, salary, commission, years_of_experience, technology)

def insert_employee():
    employee = read_employee_details()
    query = '''
    INSERT INTO employee(name, designation, phone_number, salary, commission, years_of_experience, technology)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query, employee)
            connection.commit()
            print('Employee inserted successfully')
            cursor.close()
        except pymysql.MySQLError as e:
            print(f'Row insertion failed: {e}')
        finally:
            disconnect_db(connection)

def update_employee():
    emp_id = int(input('Enter the ID of the employee to update: '))
    salary = float(input('Enter new salary: '))
    years_of_experience = int(input('Enter new years of experience: '))
    query = 'UPDATE employee SET salary = %s, years_of_experience = %s WHERE id = %s'
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            rows_updated = cursor.execute(query, (salary, years_of_experience, emp_id))
            connection.commit()
            if rows_updated:
                print(f'Employee with ID {emp_id} updated successfully')
            else:
                print(f'No employee found with ID {emp_id}')
            cursor.close()
        except pymysql.MySQLError as e:
            print(f'Update failed: {e}')
        finally:
            disconnect_db(connection)

def delete_employee():
    emp_id = int(input('Enter the ID of the employee to delete: '))
    query = 'DELETE FROM employee WHERE id = %s'
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            rows_deleted = cursor.execute(query, (emp_id,))
            connection.commit()
            if rows_deleted:
                print(f'Employee with ID {emp_id} deleted')
            else:
                print(f'No employee found with ID {emp_id}')
            cursor.close()
        except pymysql.MySQLError as e:
            print(f'Deletion failed: {e}')
        finally:
            disconnect_db(connection)
