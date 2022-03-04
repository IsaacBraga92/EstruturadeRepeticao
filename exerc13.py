# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

base = int(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))

potencia = 1

for aux in range(expoente):
    potencia *= base
    aux += 1

print(f"{base}^{expoente}={potencia}")
