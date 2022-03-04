# Faça um programa que leia 5 números e informe a soma e a média dos números.

aux = 0
soma=0
while aux < 5:
    aux += 1
    n = float(input("Informe um número: "))
    soma = soma+n

media=soma/aux

print(f"A soma dos números é: {soma}")
print(f"A media dos números é {media}")