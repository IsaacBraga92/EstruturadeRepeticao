'''
    Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
    representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto
    e o número do aluno mais baixo, junto com suas alturas.
'''
import random
from cmath import inf

maior_altura = -inf
menor_altura = inf
id_aluno = 0
id_maior_altura = 0
id_menor_altura = 0
for i in range(10):
    id_aluno = i + 1
    altura = random.randint(40, 220)
    if altura > maior_altura:
        maior_altura = altura
        id_maior_altura = i + 1
    if altura < menor_altura:
        menor_altura = altura
        id_menor_altura = i + 1

print(f"O número de matricula do aluno mais alto é: {id_maior_altura} e ele tem {maior_altura} centimetros de altura.")
print(f"O número de matricula do aluno mais baixo é: {id_menor_altura} e ele tem {menor_altura} centimetros de altura.")
