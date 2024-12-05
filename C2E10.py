def main():
    firstName = input("enter your first name: ")
    lastName = input("Enter your last name: ")
    print(f'Your name is {firstName, lastName}')



COOKIES_RECIPE = 48.0
SUGAR_RECIPE = 1.5
BUTTER_RECIPE = 1.0
FLOUR_RECIPE = 2.75
cookies = int(input("Enter number of cookies desired: "))
sugar = cookies / COOKIES_RECIPE * SUGAR_RECIPE
butter = cookies / COOKIES_RECIPE * BUTTER_RECIPE
flour = cookies / COOKIES_RECIPE * FLOUR_RECIPE
print(f"To make (cookies) cookies you will need: ")
print(f"{sugar:.2f} cups of sugar")
print(f"{butter:.2f} cups of butter")
print (f"{flour:.2f} cups of flour")


main()
