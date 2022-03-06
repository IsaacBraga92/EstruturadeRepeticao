# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
# por quais número ele é divisível.

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
