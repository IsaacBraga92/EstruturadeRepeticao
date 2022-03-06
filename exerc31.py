'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então
calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a
próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
'''
n = 1
total = 0
while True:
    preco = float(input(f"Informe o valor do produto {n}: "))
    n+=1
    total+=preco
    if preco ==0:
        break

print(f"O valor total da compra é: R${total}")
dinheiro = float(input("Dinheiro: R$ - "))
while dinheiro<total:
    print("Dinheiro insulficiente!")
    dinheiro = float(input("Dinheiro: R$ - "))
troco = dinheiro-total
print(f"O seu troco é: R$ - {troco}")


