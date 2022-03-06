# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
# quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
import random

quantidade_turmas = random.randint(1, 100)
auxiliar = 0
soma = 0
while auxiliar < quantidade_turmas:
    quantidade_alunos = random.randint(1, 40)
    soma += quantidade_alunos
    auxiliar += 1

media = soma / quantidade_turmas
media = int(media)
print(f"A media de alunos por turma é {media}")
