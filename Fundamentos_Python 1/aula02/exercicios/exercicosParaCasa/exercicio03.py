#Divisão inteira e resto 

numero1 = float(input("Digite um numero para a divisão:"))
divisor = float(input("Digite o numero para dividir:"))
divisaoInterira = numero1/divisor
restoDivisao = numero1%divisor

print(f"A divisão do numero {numero1}/{divisor}={divisaoInterira}")
print(f"O resto da divisão de {numero1} é {restoDivisao}")