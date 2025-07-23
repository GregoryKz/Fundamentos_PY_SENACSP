

def imparPar (numero1):
    resultado = numero1%2
    if (resultado == 0):
        print(" O numero é par ")
    else:
        print("Impar")

        
numero1 = int(input("Digite um numero:"))
imparPar(numero1)