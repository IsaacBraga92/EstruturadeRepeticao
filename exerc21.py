# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("Informe um número: "))
contador = 0
for n in range(1, numero + 1):
    if numero % n == 0:
        contador += 1

if contador == 2:
    print("O número é primo!")
else:
    print(f"Tem {contador} acima de dois.")
