# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
# população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
# número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as
# taxas de crescimento.

pais_a = 80_000
pais_b = 200_000
anos = 0
while pais_a < pais_b:
    pais_a += round((pais_a*3)/100)
    pais_b += round((pais_b*1.5)/100)
    anos += 1
else:
    print(f"Anos necessário para alcançar a quantidade de população: {anos}")
    print(f"Habitantes País A: {pais_a}")
    print(f"Habitantes País B: {pais_b}")
