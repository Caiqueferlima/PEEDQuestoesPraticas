x = int(input("Quantos números você irá informar? "))

lista = []

for c in range(x):
    n = float(input("Informe o valor: "))
    lista.append(n)
lista.sort()

print(f"O maior valor informado é {lista[x-1]}.")