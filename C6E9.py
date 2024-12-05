def calculate_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = []
            for line in file:
                try:
                    number = int(line.strip())
                    numbers.append(number)
                except ValueError:
                    print("Error: Invalid value found in file.")
                    continue
            average = sum(numbers) / len(numbers)
            print("Average of numbers:", average)
    except IOError:
        print("Error: File not found or could not be opened.")



calculate_average("numbers.txt")
