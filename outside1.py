
#essa e a funcao
def area(larg, comp): #o (larg, comp) dentro dos parenteses representa meio que a chamada da funcao dentro dela, por isso que na linha abaixo temos o a = larg x comp
    a = larg * comp
    print(f"A area de um terreno {larg} x {comp} e de {a}m2.")


#embelezando o texto
print("Controle de Terrenos")
print("-"*20)

#definindo as variaveis que irao receber os valores
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))

#chamando a funcao:
area(l, c)
