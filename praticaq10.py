x = int(input("Quantos números você ira informar? Irei informar a média da soma deles. "))
soma = 0
lista = []
cont = 0

for c in range(x):
    y = float(input("Informe um valor:"))
    lista.append(y)
    soma += y
print("A media da soma dos números: ", end="")

for c in lista:
    if cont < x - 2:
        print(f"{c}, ", end="")
    elif cont < x - 1:
        print(f"{c} ", end="")
    elif cont < x:
        print(f"e {c} ", end="")
    cont += 1

print(f"é igual a {soma/x}.")