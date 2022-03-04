#   Faça um programa que leia 5 números e informe o maior número.

maior = float(input("Informe um número: "))
for _ in range(4):
    maior = max(maior, float(input("Informe um número: ")))

print(f"O maior número é: {maior}")
