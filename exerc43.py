'''
O cardápio de uma lanchonete é o seguinte:

                Especificação   Código  Preço
                Cachorro Quente 100     R$ 1,20
                Bauru Simples   101     R$ 1,30
                Bauru com ovo   102     R$ 1,50
                Hambúrguer      103     R$ 1,20
                Cheeseburguer   104     R$ 1,30
                Refrigerante    105     R$ 1,00

    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago
    por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve
    ser encerrado.
'''
import random

id_pedido = 0
# Criando contador para os produtos
quantidade_cachorro_quente = 0
quantidade_bauru_simples = 0
quantidade_bauru_com_ovo = 0
quantidade_hamburguer = 0
quantidade_cheeseburguer = 0
quantidade_refrigerante = 0

while True:
    id_pedido = int(input("Informe o lanche que você quer: "))
    if id_pedido not in [100, 101, 102, 103, 104, 105]:
        break
    if id_pedido == 100:
        quantidade_cachorro_quente += int(input("Quantos Cachorros Quente você vai querer? "))
    if id_pedido == 101:
        quantidade_bauru_simples += int(input("Quantos Baurus Simples você vai querer? "))
    if id_pedido == 102:
        quantidade_bauru_com_ovo += int(input("Quantos Baurus com ovo você vai querer?"))
    if id_pedido == 103:
        quantidade_hamburguer += int(input("Quantos Hambúrgueres você vai querer? "))
    if id_pedido == 104:
        quantidade_cheeseburguer += int(input("Quantos Cheesebúrguers você vai querer? "))
    if id_pedido == 105:
        quantidade_refrigerante += int(input("Quantos Refrigerantes você vai querer? "))

valor_total = (quantidade_cachorro_quente * 1.2) + (quantidade_bauru_simples * 1.3) + (
        quantidade_bauru_com_ovo * 1.5) + (quantidade_hamburguer * 1.2) + (quantidade_cheeseburguer * 1.3) + (
                      quantidade_refrigerante * 1)

print(f"O valor total do pedido é: {valor_total}")
