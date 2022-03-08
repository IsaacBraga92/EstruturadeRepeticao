"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    A - Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    B - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    C- A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um
        programa que determine o salário atual desse funcionário.
        Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""

ano_contratado = 1995
salario_inicial = float(input("Informe o salário inicial: "))
aumento_salarial_inicial = 1.5
contador = 1
salario_atual = 0
ano_atual = int(input("Informe o ano ao qual estamos: "))
while ano_atual < ano_contratado:
    print("O ano atual tem que sair maior que o ano de contrato!")
    ano_atual = int(input("Informe o ano ao qual estamos: "))

for i in range(ano_contratado+1,ano_atual+1):
    salario_atual = salario_inicial + ((aumento_salarial_inicial/100) * salario_inicial)
    salario_inicial = salario_atual
    aumento_salarial_inicial = aumento_salarial_inicial*2
    print(f"Ano - {i}: salário: {round(salario_atual,2)} recebeu aumento salárial de {aumento_salarial_inicial}%.")
