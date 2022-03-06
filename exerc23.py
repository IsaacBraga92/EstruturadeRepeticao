# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O
# programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão
# avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

numero = int(input("Informe um número: "))
contador = 0
for n in range(1, numero + 1):
    if numero % n == 0:
        print(f"O número {numero} é múltiplo de {n}")
        contador += 1

if contador == 2:
    print("O número é primo!")
else:
    print(f"Tem {contador} divisores.")