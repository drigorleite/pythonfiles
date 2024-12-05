def sumOfDigits():
    string = input("Enter a series of single-digit numbers: ")
    return sum(int(char) for char in string if char.isdigit())


print(sumOfDigits())
