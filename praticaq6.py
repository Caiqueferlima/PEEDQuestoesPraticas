print("Me indique vários números, vou somá-los!")
quantNum = int(input("Digite quantos números serão: "))
soma = 0

for n in range(quantNum):
    c = int(input(f"Número {n+1}: "))
    soma = c
    soma = soma + c

print("A soma deles é", soma)