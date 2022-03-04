# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input('Infomer o primeiro número inteiro: '))
n2 = int(input('Infomer o segundo número inteiro: '))

if n1 < n2:
    for num in range(n1, n2):
        print(num, end=' ')
elif n2 < n1:
    for num in range(n2, n1):
        print(num, end=' ')
else:
    print("Os números são iguais!")
