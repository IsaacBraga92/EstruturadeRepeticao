# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
# turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
# média calculada.
import random

quantidade = int(input("Informe a quantidade de pessoas: "))
auxiliar = 0
soma_idade = 0
while auxiliar < quantidade:
    idade = random.randint(0, 100)
    soma_idade += idade
    auxiliar += 1
    print(f"A idade da pessoa de número {auxiliar} é {idade} anos.")

media_idade = soma_idade / auxiliar
media_idade = int(media_idade)

print(f"A media de idade é: {media_idade}")

if media_idade == 0 or media_idade < 26:
    print("A turma é classificada como jovem de acordo com a media de idade!")
elif media_idade == 26 or media_idade < 61:
    print("A turma é classificada como adulta de acordo com a media de idade!")
elif media_idade > 60:
    print("A turma é classificada como idosa de acordo com a media de idade!")
