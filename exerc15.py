# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

numero = int(input("Qual termo deseja encontrar? "))
ultimo = 0
penultimo = 1

if (numero ==1) or (numero ==2):
    print("1")
else:
    for auxiliar in range(0,numero):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        auxiliar+=1
        print(termo, end=' ')
