class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_rate):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__hourly_rate = hourly_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_rate(self):
        return self.__hourly_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate



def main():
    name = input("Enter the employee's name: ")
    number = input("Enter the employee number: ")
    shift_number = int(input("Enter the shift number (1 for day, 2 for night): "))
    hourly_rate = float(input("Enter the hourly pay rate: "))

    worker = ProductionWorker(name, number, shift_number, hourly_rate)

    print("\nEmployee Information:")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_number())
    print("Shift Number:", worker.get_shift_number())
    print("Hourly Rate: ${:.2f}".format(worker.get_hourly_rate()))

main()
