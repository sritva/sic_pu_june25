# main.py

import employee_crud_mysql1_fixed as emp
print(dir(emp))  # Lists all available functions and variables in the module


def menu(choice):
    match choice:
        case 1: emp.insert_employee()
        case 2: emp.delete_employee()
        case 3: emp.update_employee()
        case 4: emp.search_employee()
        case 5: emp.read_all_employees()
        case 6: pass  
        case _: print('Invalid Choice')

def start_app():
    print('--- EMPLOYEE MANAGEMENT SYSTEM ---')
    while True:
        try:
            choice = int(input('1:Insert 2:Delete 3:Update 4:Search 5:List All 6:Exit \nYour Choice: '))
            if choice == 6:
                break
            menu(choice)
        except ValueError:
            print("Please enter a valid number.")
    print('Application closed')

# WHY this is needed:
# This prevents the code from running automatically if this file is imported into another module
if __name__ == '__main__':
    start_app()
