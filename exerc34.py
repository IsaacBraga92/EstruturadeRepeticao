# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro
# e determine se ele é ou não um número primo.

numero = int(input("Informe um número: "))
contador = 0
lista_nao_primos =[]
for n in range(1, numero + 1):
    if numero % n == 0:
        contador += 1
if contador == 2:
    print(f"O número {numero} é primo!")
else:
    print(f"Tem {contador} divisores, logo não é primo.")
