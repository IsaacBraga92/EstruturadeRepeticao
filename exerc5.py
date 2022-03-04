# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

pais_a = int(input("Informe a população do país A: "))
while pais_a < 1:
    print("A população deve ser maior que zero!")
    pais_a = int(input("Informe a população do país A: "))

taxa_pais_a = float(input("Informe a taxa de crescimento do país A: "))
while taxa_pais_a < 0:
    print("A taxa de crescimento precisa ser maior que zero!")
    taxa_pais_a = float(input("Informe a taxa de crescimento do país A: "))

pais_b = int(input("Informe a população do país B: "))
while pais_b < 1:
    print("A população deve ser maior que zero!")
    pais_b = int(input("Informe a população do país B: "))

taxa_pais_b = float(input("Informe a taxa de crescimento do país B: "))
while taxa_pais_b < 0:
    print("A taxa de crescimento precisa ser maior que zero!")
    taxa_pais_b = float(input("Informe a taxa de crescimento do país B: "))

anos = 0
while pais_a < pais_b:
    pais_a += round((pais_a * taxa_pais_a) / 100)
    pais_b += round((pais_b * taxa_pais_b) / 100)
    anos += 1
else:
    print(f"Anos necessário para alcançar a quantidade de população: {anos}")
    print(f"Habitantes País A: {pais_a}")
    print(f"Habitantes País B: {pais_b}")
