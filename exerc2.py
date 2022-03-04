# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str(input("Informe o nome de usuário: "))
senha = str(input("Informe a senha: "))

while nome == senha:
    print("A senha não pode ser igual ao nome de usuário.")
    nome = str(input("Informe o nome de usuário: "))
    senha = str(input("Informe a senha: "))
else:
        print("Usuário cadastrado com sucesso! ")
        print(f"O nome de usuário é: {nome}")
        print(f"A senha de usuário é: {senha}")
