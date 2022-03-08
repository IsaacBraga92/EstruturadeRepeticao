# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
# seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um
# número negativo.
import random

contador0_25 = 0
contador26_50 = 0
contador51_75 = 0
contador76_100 = 0

while True:
    numero = random.randint(-1, 100)
    if numero < 0:
        break
    if 0 < numero < 26:
        contador0_25 += 1
    elif 25 < numero < 51:
        contador26_50 += 1
    elif 50 < numero < 76:
        contador51_75 += 1
    elif 75 < numero < 101:
        contador76_100 += 1

print(f"A quantidade de números entre 0 - 25 é {contador0_25}")
print(f"A quantidade de números entre 26 - 50 é {contador26_50}")
print(f"A quantidade de números entre 51 - 75 é {contador51_75}")
print(f"A quantidade de números entre 76 - 100 é {contador76_100}")

