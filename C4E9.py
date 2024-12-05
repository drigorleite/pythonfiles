# Ocean Level Rise Calculator

rise_rate = 1.6
years = 25

print("Year  Ocean Level (mm)")
print("------------------------")

year = 1
while year <= years:
    ocean_level = year * rise_rate
    print(f"{year:.2f} ----- {ocean_level:.2f}")
    year += 1
