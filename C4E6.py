#celsius to fahrenheit

print("CELSIUS TO FAHRENHEIT TABLE")

# Display table headers
print("Celsius   Fahrenheit")
print("---------------------")

# Display temperature conversions for Celsius 0 through 20
for celsius in range(21):
    fahrenheit = 9.0 / 5.0 * celsius + 32
    print(f"{celsius:.0f} ------ {fahrenheit:.0f}")
