# Faça um programa que calcule o mostre a média aritmética de N notas.
import random

n = int(input("Informe a quantidade de notas: "))

auxiliar = 0
soma = 0
while auxiliar < n:
    nota = random.uniform(0.0, 10.0)
    soma += round(nota, 2)
    auxiliar += 1
    print(f"A nota de número {auxiliar} foi: {round(nota, 2)}")
media = soma / auxiliar
print(f"Media: {round(media, 2)}")
print(f'{media:,.3}')
