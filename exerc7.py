#   Faça um programa que leia 5 números e informe o maior número.
aux = 0
maior = 0
while aux < 5:
    aux += 1
    n = float(input("Informe um número: "))
    if n > maior:
        maior = n

print(f"O maior número é: {maior}")
