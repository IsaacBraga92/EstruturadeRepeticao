# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre
# 1 e um número inteiro informado pelo usuário.
import random

numero_fornecido = random.randint(1, 100)
contador = 0
lista = []
numero = numero_fornecido
auxiliar = numero
while numero > 0:
    for n in range(1, auxiliar + 1):
        if numero % n == 0:
            contador += 1
    if contador == 2:
        lista.append(numero)
    numero -= 1
    contador = 0
print(f"Os números primos entre 1 e {numero_fornecido}, são {lista}.")
