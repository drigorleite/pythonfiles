number1 = float(input("coloque o primeiro numero: "))
number2 = float(input("Numero 2: "))


calc = str(input("Voce deseja efetuar que tipo de conta? (+), (-), (*), (/): "))


if calc == '+':
    resultado = number1 + number2

elif calc == "-":
    resultado = number1 - number2

elif calc == "*":
    resultado = number1 * number2

elif calc == "/":
    resultado = number1 / number2

else:
    print('something is wrong')
    exit()

print(resultado)