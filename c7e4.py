def numberAnalysisProgram():
    numbers = []
    for _ in range(20):
        num = int(input("Enter a number: "))
        numbers.append(num)

    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print("Lowest number:", lowest)
    print("Highest number:", highest)
    print("Total of numbers:", total)
    print("Average of numbers:", average)

numberAnalysisProgram()
