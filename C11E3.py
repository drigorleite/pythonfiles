class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_telephone(self, telephone):
        self.__telephone = telephone


class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, mailing_list):
        super().__init__(name, address, telephone)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def get_customer_number(self):
        return self.__customer_number

    def is_on_mailing_list(self):
        return self.__mailing_list

    def set_customer_number(self, number):
        self.__customer_number = number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list



def customer_demo():
    name = input("Enter the person's name: ")
    address = input("Enter the address: ")
    telephone = input("Enter the telephone number: ")
    customer_number = input("Enter the customer number: ")
    mailing_list = input("Do you want to be on the mailing list? (yes/no): ").lower() == 'yes'

    customer = Customer(name, address, telephone, customer_number, mailing_list)

    print("\nCustomer Information:")
    print("Name:", customer.get_name())
    print("Address:", customer.get_address())
    print("Telephone:", customer.get_telephone())
    print("Customer Number:", customer.get_customer_number())
    print("On Mailing List:", "Yes" if customer.is_on_mailing_list() else "No")

customer_demo()
