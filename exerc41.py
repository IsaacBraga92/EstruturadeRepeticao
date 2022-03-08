'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos
juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25
Exemplo de saída do programa:
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67
'''
divida = float(input("Informe o valor da dívida: "))
parcela = 0
juros = 0
valor_juros = 0
print("Valor da dívida: ", end='  ')
print("Valor do juros: ",end='  ')
print("Quantidade de parcelas: ",end='  ')
print("Valor da parcela: ")

for i in range(5):
    if parcela == 0:
        juros = 0
    elif parcela == 3:
        juros = 0.1
    elif parcela == 6:
        juros = 0.15
    elif parcela == 9:
        juros = 0.2
    elif parcela == 12:
        juros = 0.25

    valor_juros = divida*juros
    divida_mais_juros = divida + valor_juros
    if parcela ==0:
        parcela +=1
        valor_parcelas = divida_mais_juros / parcela
        parcela = 0
    else:
        valor_parcelas = divida_mais_juros / parcela
    print("R$: ", round(divida_mais_juros,2), end='          ')
    print(round(valor_juros,2),end='                ')
    if parcela == 0:
        parcela = 1
        print(parcela, end='                                     ')
        parcela = 0
    else:
        print(parcela, end='                              ')
    print("R$: ", round(valor_parcelas,2))
    parcela+=3


