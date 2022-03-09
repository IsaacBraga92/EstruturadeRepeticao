# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
# até que o usuário informe um valor válido.


while True:
    try:
        numero = int(input("Informe um numero entre 0 e 10: "))
    except ValueError:
        print("Deve ser fornecido um valor inteiro.")
    else:
        if 0<= numero <=10:
            print(f"O número informado é {numero}.")
            break
        else:
            print("O numero informado deve estar entre 0 e 10")