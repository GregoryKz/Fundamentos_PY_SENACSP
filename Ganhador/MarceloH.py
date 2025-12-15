# Crie um programa que cadastre 3 alunos
# Para cada aluno, peça o nome e 2 notas
# Calcule a média
# Diga se o aluno foi APROVADO (média ≥ 7) ou REPROVADO
# Mostre no final um resumo com nome, notas, média e situação

print ("Cadastro de alunos para média de notas")
aluno1 = input("Qual o seu nome?")

def media(nota1,nota2):
  resultadoMedia = (nota1+nota2)/2
  print(resultadoMedia)
nota1 = float(input("Digite sua 1ª nota"))
nota2 = float(input("Digite sua 2ª nota"))
media(nota1,nota2)

if(media>=7):
    print("Aprovado!")
elif(nota1>=5 and nota2<=6.9):
    print("Você está de recuperação!")
else:
    print("Reprovado")