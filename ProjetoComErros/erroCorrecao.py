# Exercício 1: Print simples
# ERRO: aspas estavam incorretas
print("Olá mundo")

# Exercício 2: Soma de dois números
# ERRO: concatenação sem conversão para string
a = 10
b = 20
soma = a + b
print("A soma é: " + str(soma))

# Exercício 3: Verificar se número é par
# ERRO: uso de '=' ao invés de '==' e falta de ':'
numero = 7
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# Exercício 4: Lista e loop
# ERRO: range(lista) estava errado
lista = [1, 2, 3, 4, 5]
for i in range(len(lista)):
    print(lista[i])

# Exercício 5: Fatorial de um número
# ERRO: retornava 'i' em vez de 'fat'
def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat
print(fatorial(5))

# Exercício 6: Contar vogais em uma string
# ERRO: soma final estava errada (+1)
texto = "Exercicio com Erros"
vogais = "aeiouAEIOU"
cont = 0
for letra in texto:
    if letra in vogais:
        cont += 1
print("Quantidade de vogais:", cont)

# Exercício 7: Verifica se número está em lista
# ERRO: expressão booleana mal formada
numeros = [10, 20, 30, 40]
if 50 in numeros:
    print("Número encontrado")
else:
    print("Número não está na lista")

# Exercício 8: Calcular média de notas
# ERRO: else estava sem indentação correta
notas = [7.5, 8.0, 6.5]
media = sum(notas) / len(notas)
if media > 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Exercício 9: Verificar se string é palíndromo
# ERRO: palavra "palíndrommo" escrita errada
palavra = "arara"
if palavra == palavra[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

# Exercício 10: Criar dicionário com dados de pessoa
# ERRO: chave 'nome' sem aspas
pessoa = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "São Paulo"
}
print(pessoa["nome"])

# Exercício 11: Verificar maior número em lista
# ERRO: maior inicializado com 0, o que pode falhar com números negativos
lista = [1, 2, 3, 4, 5]
maior = lista[0]
for num in lista:
    if num > maior:
        maior = num
print("Maior número é", maior)

# Exercício 12: Soma dos pares em uma lista
# ERRO: somando ímpares em vez de pares
valores = [1, 2, 3, 4, 5, 6]
soma_pares = 0
for v in valores:
    if v % 2 == 0:
        soma_pares += v
print("Soma dos pares:", soma_pares)

# Exercício 13: Função que retorna elementos únicos
# ERRO: adicionava lista inteira em vez de item
def unicos(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista
print(unicos([1, 2, 2, 3, 4, 4]))

# Exercício 14: Conversão de temperatura
# ERRO: passava string ao invés de número
def celsius_para_fahrenheit(c):
    return (c * 9 / 5) + 32
print(celsius_para_fahrenheit(30))

# Exercício 15: Função recursiva de Fibonacci
# ERRO: passava número decimal (float), deve ser inteiro
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))
