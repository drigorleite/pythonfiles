def calculate_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            average = sum(numbers) / len(numbers)
            print("Average of numbers:", average)
    except IOError:
        print("Error: File not found or could not be opened.")
    except ValueError:
        print("Error: Invalid value found in file.")


calculate_average("numbers.txt")
