'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
    A - Código da cidade;
    B - Número de veículos de passeio (em 1999);
    C - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    D - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    E - Qual a média de veículos nas cinco cidades juntas;
    F - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''
import random
from cmath import inf

id_cidade = 0
maior_indice_acidentes = -inf
menor_indice_acidentes = inf
cidade_maior_indice = 0
cidade_menor_indice = 0
soma_menor_2000 = 0
contador_cidade_menor_2000 = 0
soma_veiculos_cidade = 0
while True:
    if id_cidade == 5:
        break
    for id_cidade in range(1,6):
        numero_veiculos_passeio = random.randint(100, 7500)
        numero_acidentes = random.randint(10, 500)
        soma_veiculos_cidade += numero_veiculos_passeio
        if numero_veiculos_passeio < 2000:
            soma_menor_2000 += numero_veiculos_passeio
            contador_cidade_menor_2000 += 1
        if numero_acidentes > maior_indice_acidentes:
            maior_indice_acidentes = numero_acidentes
            cidade_maior_indice = id_cidade
        if numero_acidentes < menor_indice_acidentes:
            menor_indice_acidentes = numero_acidentes
            cidade_menor_indice = id_cidade
        print(f"Cidade - {id_cidade} | quantidade de veículos {numero_veiculos_passeio}")
media_veiculos_cidade = soma_veiculos_cidade/ 5
media_veiculos_cidade_menor_2000 = soma_menor_2000/contador_cidade_menor_2000
print(f"O maior íncide de acidentes de trânsito pertence a cidade {cidade_maior_indice} e equivale a {maior_indice_acidentes}")
print(f"O menor íncide de acidentes de trânsito pertence a cidade {cidade_menor_indice} e equivale a {menor_indice_acidentes}")
print(f"A média de veículos entre as cinco cidades é de {media_veiculos_cidade}")
print(f"A média de veículos entre as cidades com menos de 2000 veículos é de {media_veiculos_cidade_menor_2000}")
