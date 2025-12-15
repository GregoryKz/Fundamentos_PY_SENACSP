usuarios = {}
def cadstrar():
    nome = input("Digite o nome do usuario: ")
    if nome in usuarios:
        print("Nome do usuario  já existente. Tente outro.")
        return
    senha = input("DIgite sua senha:")
    usuarios[nome] = senha
    print("Usuario cadastrar coom secusso!")


def login ():
    nome = input("Digite o nome do usuario:")
    senha = input("Digite a senha:")
    if nome in usuarios and usuarios[nome] == senha:
        print(f"Bem vindo, {nome}!")
    elif nome in usuarios:
        print("Senha incorreta.")
    else:
        print("Usuario não encontrado.")

def menu ():
    while True:
        print("Menu")
        print("!. Cadastrar")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção:")
        if opcao == "1":
            cadstrar()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção invalida. Tente novamente.")


menu()