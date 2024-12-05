from time import sleep

def contador(i, f, p):
    print(f"Contagem de {i} ate {f} de {p} em {p}.")
    sleep(1.5)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = 1
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print("FIM!")

contador(1, 10, 1)
contador(20, 0, 2)
print("Agora e a sua vez de personalizar a contagem: ")
ini =  int(input("Inicio: "))
fim = int(input("FIM: "))
passo = int(input("Passo: "))
contador(ini, fim, passo)
