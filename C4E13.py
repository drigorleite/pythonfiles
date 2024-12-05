#population

s_pop = int(input("Enter the starting number of organisms: "))
daily = float(input("Enter the average daily population increase (as a percentage): "))
days = int(input("Enter the number of days the organisms will be left to multiply: "))


print("Day ------------------ Approximate Population")

# Calculate and display population for each day
for day in range(1, days + 1):
    population = s_pop * (1 + daily / 100) ** day
    print(f"{day} ------------------ {population:.2f}")
