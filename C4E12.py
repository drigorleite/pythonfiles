#Calculating the Factorial of a Number

user_input = input("Enter a nonnegative integer: ")


if user_input.isdigit():
    num = int(user_input)
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    # Display the factorial
    print(f"The factorial of {num} is {factorial}")
else:
    print("Please enter a valid nonnegative integer.")
