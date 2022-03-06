# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
# gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
import random

quantidade_de_cds = random.randint(10,10000)
auxiliar = 0
soma = 0
for auxiliar in range(0,quantidade_de_cds):
    valor_do_cd = random.uniform(0,1000)
    soma += valor_do_cd
    auxiliar +=1

media = soma / auxiliar
print(f"Com a coleção de {quantidade_de_cds} CDs e um investimento total de R$:{round(soma,2)}.")
print(f"A media de valor gasto em cada CD da coleção foi de R$:{round(media,2)}")

