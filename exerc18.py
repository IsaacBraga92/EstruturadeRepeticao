# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a
# soma dos valores.
import random

menor = maior = 0
aux = 0
quantidade = int(input("Informe a quandidade de numeros a serem inseridos: "))

while aux < quantidade:
    n = random.randint(1, 100)
    print(n, end=' ')
    if menor == 0:
        menor = n
    elif menor >= n:
        menor = n
    if maior == 0:
        maior = n
    elif maior <= n:
        maior = n
    aux += 1

print(f"\nO menor número é {menor} e o maior número é {maior}.")
soma = menor + maior
print(f"A soma do menor número com o maior é igual a {soma}")
