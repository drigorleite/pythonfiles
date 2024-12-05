
print("COLOR MIX")

red = "red"
blue = "blue"
yellow = "yellow"

print("Choose a primary color to mix: RED, BLUE or YELLOW")
choice = input(str("Enter the first color that you want to mix: ")).lower()
choice2 = input(str("Enter the second color that you want to mix: ")).lower()

if choice == "red" and choice2 == 'blue':
    print("Your mix result is: Purple")
elif choice == "red" and choice2 == 'yellow':
    print("Your mix result is: Orange")
elif choice == "blue" and choice2 == "yellow":
    print("Your mix result is: Green.")
