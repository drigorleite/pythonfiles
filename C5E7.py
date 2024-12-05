def calculate_income(class_a, class_b, class_c):
    class_a_income = class_a * 20
    class_b_income = class_b * 15
    class_c_income = class_c * 10
    total_income = class_a_income + class_b_income + class_c_income
    return total_income


class_a_tickets = int(input("Enter the number of Class A tickets sold: "))
class_b_tickets = int(input("Enter the number of Class B tickets sold: "))
class_c_tickets = int(input("Enter the number of Class C tickets sold: "))

total_income = calculate_income(class_a_tickets, class_b_tickets, class_c_tickets)

print(f"Total income generated: ${total_income:.2f}")
