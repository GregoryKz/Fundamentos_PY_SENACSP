alunos = []  
# Criando lista vazia para utilizar depois

quantidade = int(input("Quantos alunos deseja cadastrar?:"))  
# Criando uma variavel para dizer quantas vezes o for ira executar

for i in range(quantidade):  
    # Iniciando um laço de repetição que vai repetir a quantidade da nossa variavel(quantidade) 

    print(f"Cadastro do aluno {i + 1}º aluno: ")  
    # Exibe uma mensagem indicando o número do cadastro do aluno atual (i+1 para começar do 1, não do 0).

    nome = input("Nome do aluno:")  
    # Solicita que o usuário informe o nome do aluno atual.

    nota1 = float(input("Digite a nota da primeira prova:"))  
    # Solicita a primeira nota do aluno e converte a entrada para um número decimal (float).

    nota2 = float(input("Digite a nota da segunda prova:"))  
    # Solicita a segunda nota do aluno e converte a entrada para float.

    media = (nota1 + nota2) / 2  
    # Calcula a média aritmética entre as duas notas.

    if media >= 7:  
        status = "APROVADO"  
    else:  
        status = "REPROVADO"  
    # Verifica se a média é maior ou igual a 7, definindo o status como 'APROVADO' ou 'REPROVADO'.

    aluno = {  
        "nome": nome,  
        "nota1": nota1,  
        "nota2": nota2,  
        "media": media,  
        "status": status  
    }  
    # Cria um dicionário com as informações do aluno, incluindo nome, notas, média e status.

    alunos.append(aluno)  
    # Adiciona o dicionário do aluno atual à lista 'alunos'.

print("Fechamento")  
# Imprime um título para indicar o início da listagem final dos alunos cadastrados.

for aluno in alunos:  
    # Percorre a lista de alunos para imprimir os dados de cada um.

    print(f"Aluno: {aluno['nome']} - Média: {aluno['media']} - Status: {aluno['status']}")  
    # Exibe o nome, a média e o status do aluno formatados em uma única linha.
