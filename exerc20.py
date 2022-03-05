# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular
# o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
while 1 == 1:
    fatorial = 1
    numero = int(input("Informe um numero maior que 1 e menor que 16: "))
    if numero == 000:
        break
    while numero >16 or numero<0:
        numero = int(input("Informe um numero maior que 1 e menor que 16: "))
    else:
        while numero != 1:
            fatorial *= numero
            numero -= 1
            print(fatorial)
    print("Para sair digite 000")

