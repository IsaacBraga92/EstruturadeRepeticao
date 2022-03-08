"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e
    o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, 
    sua altura e seu peso.
    O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa 
    também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro,
    além da média das alturas e dos pesos dos clientes
"""
import random
from cmath import inf

menor_peso = inf
maior_peso = -inf
menor_altura = inf
maior_altura = -inf
id_maior_peso = 0
id_menor_peso = 0
id_maior_altura = 0
id_menor_altura = 0
numero_alunos = 0

total_peso = 0
total_altura = 0

while True:
    id_aluno = int(input("Informe o seu código de matricula: "))
    if id_aluno == 0:
        break

    # altura = int(input("Informe sua altura em centímetros: "))
    altura = random.randint(100, 200)
    while altura < 0:
        print("Sua altura não pode ser menor que 0.")
        altura = int(input("Informe sua altura em centímetros: "))

    # peso = float(input("Informe seu peso em quilogramas: "))
    peso = random.uniform(35, 250)
    while peso < 0:
        print("Seu peso não pode ser menor que 0.")
        peso = float(input("Informe seu peso em quilogramas: "))

    total_altura += altura
    total_peso += peso

    if altura > maior_altura:
        maior_altura = altura
        id_maior_altura = id_aluno
    if altura < menor_altura:
        menor_altura = altura
        id_menor_altura = id_aluno
    if peso > maior_peso:
        maior_peso = peso
        id_maior_peso = id_aluno
    if peso < menor_peso:
        menor_peso = peso
        id_menor_peso = id_aluno

    numero_alunos += 1

media_altura = total_altura / numero_alunos
media_peso = total_peso / numero_alunos

print(f"O aluno mais alto tem {maior_altura}cm de altura e o código dele é {id_maior_altura}.")
print(f"O aluno mais baixo tem {menor_altura}cm de altura e o código dele é {id_menor_altura}")
print(f"O aluno mais pesado tem {round(maior_peso, 2)}kg de peso e o código dele é {id_maior_peso}.")
print(f"O aluno mais leve tem {round(media_peso, 2)}kg de peso e o código dele é {id_menor_peso}.")
print(f"A média da altura dos alunos é de {media_altura}cm e a média de peso é de {round(media_peso, 2)}kg")
