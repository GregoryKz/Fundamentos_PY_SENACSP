
# dicionario com o nome, notas de cada prova, média e status
Lista = []

# tela para você inserir os nomes dos 3 alunos
nome1 = str(input("Digite o primeiro nome do Aluno: "))
nome2 = str(input("Digite o segundo nome do Aluno: "))
nome3 = str(input("Digite o terceiro nome do Aluno: "))

# Dicionário com os nomes dos alunos
alunos = [nome1, nome2, nome3]

# Nome dos alunos - para conhecimento apenas
resultado = nome1, nome2, nome3

# quebra para deixar o código mais visual
print("-" * 50 )

# Mostrar os nomes dos alunos
print("Nome dos Alunos:", resultado)

#quebra para deixar o código mais visual
print("-" * 50 )

#Lista para incluir as notas de cada prova, gerar e média e checar se foi aprovado ou reprovado - e média é >= a 7
for i in alunos:
    print("Olá,", i, ",Digite as suas notas:")
    nota1 = float(input("Digite a 1ª nota da sua prova: "))
    nota2 = float(input("Digite a 2ª nota da sua prova: "))
    media = (nota1 + nota2) / 2
    if media >= 7:
        status = "aprovado"
    else:
        status = "reprovado"

#dicionario com todas as informações para gerar o resumo posteriormente     
    aluno = {
    "nome": i,
    "nota1": nota1,
    "nota2": nota2,
    "media": media,
    "situacao": status
    }

    Lista.append(aluno)
    
    print(i,media,status)

# cabeçalho para mostrar o resumo
print("-"*40)
print("Resumo Final dos Alunos:")
print("-"*40)

#resumo final contendo o nome do aluno, a nota 1 a nota 2, a média e se ele foi aprovado ou reprovado
for aluno in Lista:
    print(f"Aluno: {aluno['nome']}")
    print(f"Notas: {aluno['nota1']} e {aluno['nota2']}")
    print(f"Média: {aluno['media']}")
    print(f"Situação: {aluno['situacao']}")
    print("-"*40)
