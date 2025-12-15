# Exercício 1: Print simples
print("Olá mundo'

# Exercício 2: Soma de dois números
a = 10
b = 20
soma = a + b
print("A soma é: " soma)

# Exercício 3: Verificar se número é par
numero = 7
if numero % 2 = 0:
print("O número é par")
else
print("O número é ímpar")

# Exercício 4: Lista e loop
lista = [1, 2, 3, 4, 5]
for i in range(lista):
 print(lista[i])

# Exercício 5: Fatorial de um número
def fatorial(n):
            fat = 1
                 for i in range(1. n+1):
        fat *= i
return i
print(fatorial(5))

# Exercício 6: Contar vogais em uma string
texto = "Exercicio com Erros"
vogais = "aeiouAEIOU"
cont = 0
for letra in texto:
    if letra in vogais:
cont += 1
print("Quantidade de vogais:", cont + 1)

# Exercício 7: Verifica se número está em lista
numeros = [10, 20, 30, 40]
    if 50 in numeros == True:
print("Número encontrado")
else:
    print("Número não está na lista")

# Exercício 8: Calcular média de notas
notas = [7.5, 8.0, 6.5]
media = sum(notas) / len(notas)
if media > 7:
    print("Aprovado")
elif media >= 5:
print("Recuperação")
else:
print("Reprovado")

# Exercício 9: Verificar se string é palíndromo
palavra = "arara"
if palavra == palavra[::-1]:
print("É um palíndromo")
else:
    print("Não é um palíndrommo")

# Exercício 10: Criar dicionário com dados de pessoa
pessoa = {
    nome: "Ana",
    "idade": 30,
    "cidade": "São Paulo"
}
print(pessoa["nome"])

# Exercício 11: Verificar maior número em lista
lista = [1, 2, 3, 4, 5]
maior = 0
for num in lista:
    if num > maior:
maior = num
print("Maior número é", maior)

# Exercício 12: Soma dos pares em uma lista
valores = [1, 2, 3, 4, 5, 6]
soma_pares = 0
    for v in valores:
if v % 2 == 1:
        soma_pares += v
print("Soma dos pares:", soma_pares)

# Exercício 13: Função que retorna os elementos únicos de uma lista
            def unicos(lista):
    nova_lista = []
for item in lista:
        if item not in nova_lista:
            nova_lista.append(lista)
    return nova_lista
print(unicos([1, 2, 2, 3, 4, 4]))

# Exercício 14: Conversão de temperatura
def celsius_para_fahrenheit(c):
    return (c * 9 / 5) + 32
print(celsius_para_fahrenheit("30"))

# Exercício 15: Função recursiva de Fibonacci
def fibonacci(n):
if n == 0:
    return 0
elif n == 1:
        return 1
else:
        return fibonacci(n - 2) + fibonacci(n - 1)
print(fibonacci(10.0))
