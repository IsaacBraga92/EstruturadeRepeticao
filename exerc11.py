# Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input('Infomer o primeiro número inteiro: '))
n2 = int(input('Infomer o segundo número inteiro: '))
soma = 0
if n1 < n2:
    for num in range(n1, n2):
        soma += num
        print(num, end=' ')
elif n2 < n1:
    for num in range(n2, n1):
        soma += num
        print(num, end=' ')
else:
    print("Os números são iguais!")

print(f"\nA soma dos numeros é {soma}")
