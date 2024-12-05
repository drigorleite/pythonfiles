class Employee:
    def __init__(self, name, ID_number, department, job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title

    def display(self):
        """Prints the details of the employee."""
        print(f"Name: {self.__name}")
        print(f"ID Number: {self.__ID_number}")
        print(f"Department: {self.__department}")
        print(f"Job Title: {self.__job_title}")
        print()  # Adds a newline for better readability between entries

def main():
    # Creating instances of Employee for each specific person
    susan = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    mark = Employee("Mark Jones", 39199, "IT", "Programmer")
    joy = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    # Displaying each employee's details using the display method
    susan.display()
    mark.display()
    joy.display()

if __name__ == "__main__":
    main()
