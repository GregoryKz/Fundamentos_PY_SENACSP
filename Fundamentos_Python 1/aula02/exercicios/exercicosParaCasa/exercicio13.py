#maior numero

numero = int(input("Digite um numero:"))
numero1 = int(input("Digite outro numero:"))

if (numero> numero1):
    print(f"O maior numer é {numero}")
elif(numero == 0 and numero1 == 0):
    print("Você digitou dois numeros 0")   
else:
    print(f"O maior numero é {numero1}")