import pickle
import os

class Employee:
    def __init__(self, name, ID_number, department, job_title):
        self.name = name
        self.ID_number = ID_number
        self.department = department
        self.job_title = job_title

    def __str__(self):
        return f"Name: {self.name}, ID Number: {self.ID_number}, Department: {self.department}, Job Title: {self.job_title}"

def load_employees(filename):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def save_employees(employees, filename):
    with open(filename, 'wb') as f:
        pickle.dump(employees, f)

def add_employee(employees):
    name = input("Enter employee's name: ")
    ID_number = input("Enter employee's ID number: ")
    department = input("Enter employee's department: ")
    job_title = input("Enter employee's job title: ")
    employees[ID_number] = Employee(name, ID_number, department, job_title)

def lookup_employee(employees):
    ID_number = input("Enter employee's ID number: ")
    if ID_number in employees:
        print(employees[ID_number])
    else:
        print("Employee not found.")

def change_employee(employees):
    ID_number = input("Enter employee's ID number to update: ")
    if ID_number in employees:
        name = input("Enter the new name of the employee: ")
        department = input("Enter the new department of the employee: ")
        job_title = input("Enter the new job title of the employee: ")
        employees[ID_number].name = name
        employees[ID_number].department = department
        employees[ID_number].job_title = job_title
    else:
        print("Employee not found.")

def delete_employee(employees):
    ID_number = input("Enter employee's ID number to delete: ")
    if ID_number in employees:
        del employees[ID_number]
        print("Employee deleted.")
    else:
        print("Employee not found.")

def main():
    filename = 'employees.pkl'
    employees = load_employees(filename)

    menu = '''
    1. Look up an employee
    2. Add a new employee
    3. Change an existing employee
    4. Delete an employee
    5. Quit
    '''

    while True:
        print(menu)
        choice = input("Enter your choice: ")
        if choice == '1':
            lookup_employee(employees)
        elif choice == '2':
            add_employee(employees)
        elif choice == '3':
            change_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            save_employees(employees, filename)
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
