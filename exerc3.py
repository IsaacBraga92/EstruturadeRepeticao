# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


nome = str(input("Informe seu nome: "))
while len(nome) <= 3:
    print("O nome precisa ter mais que 3 caracteres!")
    nome = str(input("Informe seu nome: "))

idade = int(input("Informe sua idade: "))
while 0 < idade > 150:
    print("Idade precisa ser entre 0 e 150 anos!")
    idade = int(input("Informe sua idade: "))

salario = float(input("Informe seu salário: "))
while salario <= 0:
    print("O salário não pode ser menor ou igual a zero!")
    salario = float(input("Informe seu salario: "))
sexo = str(input("Informe seu sexo F-Feminino ou M-Masculino: ")).lower()
while sexo != 'f' and sexo != 'm':
    print("Sexo inválido!")
    sexo = str(input("Informe seu sexo F-Feminino ou M-Masculino: ")).lower()

estadocivil = str(input("Informe seu estado civil S-Solteiro, C-Casado, V-Viuvo, D-Divorciado(a): ")).lower()
while estadocivil != 's' and estadocivil != 'c' and estadocivil != 'v' and estadocivil != 'd':
    print("Estado civil inválido!")
    estadocivil = str(input("Informe seu estado civil S-Solteiro, C-Casado, V-Viuvo, D-Divorciado(a): ")).lower()


print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estadocivil}")
