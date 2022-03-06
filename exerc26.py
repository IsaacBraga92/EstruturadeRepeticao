# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
# votar e ao final mostrar o número de votos de cada candidato.
import random

eleitores = int(input("Informe o número total de eleitores: "))
auxiliar = 0
votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0
while auxiliar < eleitores:
    voto = random.randint(1,3)
    voto = int(voto)
    auxiliar += 1
    if voto == 1:
        votos_candidato_1 +=1
    elif voto ==2:
        votos_candidato_2+=1
    else:
        votos_candidato_3+=1

print(f"A quantidade de votos do candidato 1 foi de: {votos_candidato_1}.")
print(f"A quantidade de votos do candidato 2 foi de: {votos_candidato_2}.")
print(f"A quantidade de votos do candidato 3 foi de: {votos_candidato_3}.")