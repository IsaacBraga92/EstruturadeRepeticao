'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''
import math

n = int(input("Informe o número a ser calculado o fatorial: "))
fatorial = math.factorial(n)
auxiliar = n
while auxiliar>0:
    print(auxiliar, end= '')
    print(" . " if auxiliar>1 else ' = ', end='')
    auxiliar-=1
print(fatorial)