x = int(input("Quantos números você irá informar? "))

lista = []
for c in range(x):
    n = float(input("Informe o valor: "))
    lista.append(n)
lista.sort()

print(f"O menor valor informado é {lista[0]}.")