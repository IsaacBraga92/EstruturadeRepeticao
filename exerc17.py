# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120

numero = int(input("Informe um número inteiro: "))
fatorial = 1
while numero == 0 or numero < 0:
    print("O numero não pode ser zero.")
    numero = int(input("Informe um número inteiro: "))
while numero != 1:
    fatorial *= numero
    numero -= 1

print(fatorial)
