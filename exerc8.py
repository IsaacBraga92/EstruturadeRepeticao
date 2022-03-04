# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = float(input("Informe um número: "))
for aux in range(2, 6):
    soma += float(input("Informe um número: "))
    media = soma/aux
    print(f"A soma dos números é {soma}, e a média é {media}.")
