TIP_RATE = 0.20
TAX_RATE = 0.06

food = float(input('Please enter food charge: '))
tip = food * TIP_RATE
tax = food * TAX_RATE
total = food + tip + tax

print(f"Food: $ {food:.2f}")
print(f"Tip: $ {tip:.2f}")
print(f"Tax: $ {tax:.2f}")
print(f"Total: $ {total:.2f}")