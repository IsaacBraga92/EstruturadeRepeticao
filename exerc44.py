'''
    Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
    utilizados são:
               1, 2, 3, 4 — Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
               5 — Voto Nulo
               6 — Voto em Branco

Faça um programa que calcule e mostre:
      A — O total de votos para cada candidato;
      B — Ototal de votos nulos;
      C — O total de votos em branco;
      D — A percentagem de votos nulos sobre o total de votos;
      E — A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''
import random

jose_01 = 0
maria_02 = 0
joao_03 = 0
joana_04 = 0
nulo = 0
branco = 0
contador_votos = 0
i = 0
quantidade_de_votos = int(input("Informe a quantidade de votos: "))
while True:
    if i == quantidade_de_votos-1:
        break
    for i in range(quantidade_de_votos):
        voto = random.randint(1, 6)
        contador_votos += 1
        if voto == 1:
            jose_01 += 1
        elif voto == 2:
            maria_02 += 1
        elif voto == 3:
            joao_03 += 1
        elif voto == 4:
            joana_04 += 1
        elif voto == 5:
            nulo += 1
        else:
            branco += 1

p_nulos = ((nulo/quantidade_de_votos)*100)
p_brancos = ((branco/quantidade_de_votos)*100)
print(f"O total de votos foi: {contador_votos}")
print(f"O total de votos do candidato José foi de: {jose_01}")
print(f"O total de votos do candidata Maria foi de: {maria_02}")
print(f"O total de votos do candidato João foi de: {joao_03}")
print(f"O total de votos do candidata Joana foi de: {joana_04}")
print(f"O total de votos nulos foi de: {nulo}")
print(f"O total de votos em brancos foi de: {branco}")
print(f"A porcentagem de votos nulos foi de: {round(p_nulos)}")
print(f"A porcentagem de votos bracos foi de: {round(p_brancos)}")



