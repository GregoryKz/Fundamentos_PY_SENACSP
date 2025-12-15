usuario = ""
senha = ""

def cadastrar():
    global usuario, senha
    if usuario == "":
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        print("Cadastro feito!")
    else:
        print("Já existe um usuário cadastrado.")

def login():
    nome = input("Usuário: ")
    senha_input = input("Senha: ")
    if nome == usuario and senha_input == senha:
        print(f"Bem-vindo, {nome}!")
    elif nome == usuario:
        print("Senha incorreta.")
    else:
        print("Usuário não encontrado.")

def menu():
    while True:
        print("\n1. Cadastrar\n2. Login\n3. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()
