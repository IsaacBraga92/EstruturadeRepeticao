# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

import random

menor = maior = 0
aux = 0
quantidade = int(input("Informe a quandidade de numeros a serem inseridos: "))

while aux < quantidade:
    n = random.randint(0, 1000)
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
