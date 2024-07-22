lista = []
cont = 0
x = int(input("Quantos números você irá informar? "))

for c in range(x):
    y = int(input("Informe um valor: "))
    lista.append(y)

for c in lista:
    if c%2==0:
        print(f"{c}")