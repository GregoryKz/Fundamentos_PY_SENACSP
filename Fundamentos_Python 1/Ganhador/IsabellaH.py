print ('Programa Mini Sistema de Notas')


for contadora in range (3):

 aluno = input('Digite seu nome:')
 nota = float(input('Digite a primeira nota:'))
 nota2 = float(input('Digite a segunda nota:'))
    
 media = nota + nota2/2
 resultado = media
 
 print(f'Média: {resultado}')


 if (media>=7) :
    print('aluno aprovado')
    
 else:
    print('aluno reprovado')
    
    
 print(f'Aluno: {aluno}, Primeira nota: {nota}, Segunda nota 2: {nota2}, Média: {resultado}.' )

print(contadora) 