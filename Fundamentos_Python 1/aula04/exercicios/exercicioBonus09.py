# Cria uma lista vazia para guardar os números
numeros = []

# Pede os números até o usuário digitar 'sair'
entrada = input("Digite um número ou 'sair' para parar: ")
while entrada != "sair":
    # Converte para inteiro e guarda na lista
    numeros.append(int(entrada))
    # Pede o próximo número
    entrada = input("Digite um número ou 'sair' para parar: ")

# Mostra apenas os números pares
print("Números pares digitados:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
