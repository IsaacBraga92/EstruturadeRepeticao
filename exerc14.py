# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

aux = 1
par = 0
impar = 0
while aux in range(11):
    aux += 1
    n = int(input("Informe um número inteiro: "))
    if n % 2 == 0:
        par += 1
    elif n % 2 != 0:
        impar += 1


print(f"A quantidade de números pares é {par}")
print(f"A quantidade de números impares é {impar}")
