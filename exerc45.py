"""
    Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
    aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
    nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
    aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
    Maior e Menor Acerto;
    Total de Alunos que utilizaram o sistema;
    A Média das Notas da Turma.
        Gabarito da Prova:

        01 — A
        02 — B
        03 — C
        04 — D
        05 — E
        06 — E
        07 — D
        08 — C
        09 — B
        10 — A
    Após concluir isto poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos
    alunos usarem o programa.
"""
gabarito = ''
gabarito2 = ''
contador_1 = contador_2 = total_acertos = total = maior = menor = 0

for x in range(1, 11):
    gabarito2 = input(f"{x} - Informe a resposta do gabarito: ").strip().upper()[0]
    gabarito += gabarito2


sair = ' '
while sair not in 's':

    total_acertos = 0

    for i in range(1, 11):
        resposta = input(f" {i} - Informe a resposta de questão: ").strip().upper()[0]
        if i == 1:
            if resposta == gabarito[0]:
                contador_1 += 1
                total_acertos += 1
        if i == 2:
            if resposta == gabarito[1]:
                contador_1 += 1
                total_acertos += 1
        if i == 3:
            if resposta == gabarito[2]:
                contador_1 += 1
                total_acertos += 1
        if i == 4:
            if resposta == gabarito[3]:
                contador_1 += 1
                total_acertos += 1
        if i == 5:
            if resposta == gabarito[4]:
                contador_1 += 1
                total_acertos += 1
        if i == 6:
            if resposta == gabarito[5]:
                contador_1 += 1
                total_acertos += 1
        if i == 7:
            if resposta == gabarito[6]:
                contador_1 += 1
                total_acertos += 1
        if i == 8:
            if resposta == gabarito[7]:
                contador_1 += 1
                total_acertos += 1
        if i == 9:
            if resposta == gabarito[8]:
                contador_1 += 1
                total_acertos += 1
        if i == 10:
            if resposta == gabarito[9]:
                contador_1 += 1
                total_acertos += 1

            sair = input("Sair digite s: ").strip().lower()
            total += 1
        if total_acertos > maior:
            maior = total_acertos
        if total_acertos < menor:
            menor = total_acertos

print("Gabarito")

for x in gabarito:
    contador_2 += 1
    print(f"{contador_2} -- {x}")

print(f"Total de acertos: {contador_1}")
print(f"Pontos recebidos: {contador_1}")
print(f"Maior acerto: {maior}")
print(f"Menor acerto: {menor}")
print(f"Total de alunos a utilizar o programa: {total}")
