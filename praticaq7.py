lista = []

x = int(input("Quantas palavras você deseja informar? "))
for c in range(x):
    p = input("Escreva-as a seguir: ")
    lista.append(p)

cont = 0
for c in lista:
    
    if cont == 0:
        longa = len(c)
        indice = cont
    elif cont > 0:
        if len(c) > longa:
            longa = len(c)
            indice = cont
    cont += 1

print(f"A maior palavra informada foi {lista[indice]}!")