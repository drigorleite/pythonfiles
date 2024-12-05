#17 and 18 all together


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

user_number = int(input("Enter a number: "))
if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")

for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")
