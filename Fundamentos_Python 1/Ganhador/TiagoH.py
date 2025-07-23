#lista para armazenar os alunos
alunos = []

#cadastrar os alunos 
for i in range (3):
    print(f"Cadastro do aluno {i + 1} aluno")
    nome = input ("Nome do aluno: ")
    nota1 = float(input("Digite a nota: "))
    nota2 = float(input("Digite a nota: "))
    media = (nota1 + nota2)/2

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    #salvar os dados dentro do dicionário
    aluno = {"Nome": nome, 
             "nota1": nota1, 
             "nota2": nota2, 
             "media": media, 
             "situacao": situacao}
    #adiciona o aluno dentro da lista
    alunos.append(aluno)

# exibir o nome, notas, média e situação do aluno    
print(f"Nome: {aluno}")
print(f"Notas: {nota1} e {nota2}")
print(f"Média: {media}")
print(f"Situação: {situacao}")