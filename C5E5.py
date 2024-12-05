#Property tax

pieceOfProperty = float(input("Insert your land value: "))

taxes = pieceOfProperty * 0.000072
assesmentValue = pieceOfProperty * 0.6
taxCalc = (assesmentValue // 100) * taxes

print(f"Your property tax is ${taxCalc:.2f} and its assesment value is ${assesmentValue:.2f}")