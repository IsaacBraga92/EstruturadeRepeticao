'''
 O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
 de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
'''
from math import inf
maior = -inf
menor = inf
soma = 0
auxiliar = 0
print("Programa para ler as temperaturas para sair digite: SAIR.")
while True:
    temperatura = (input("Informe a temperatura: ")).lower()
    if temperatura == 'sair':
        break

    temperatura = float(temperatura)
    auxiliar +=1
    soma += temperatura
    if temperatura < menor:
        menor=temperatura
    if temperatura > maior:
        maior = temperatura
media_temperatura = soma / auxiliar
print(f"A maior temperatura foi de {maior}°.")
print(f"A menor temperatura foi de {menor}°.")
print(f"A média de  temperatura foi de {round(media_temperatura,2)}°.")

