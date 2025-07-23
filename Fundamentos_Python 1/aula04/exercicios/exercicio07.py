#Objetivo: Mostrar um menu até a pessoa digitar “sair”
menu = input("Digite sair")

while menu != "sair":
    print("Opção errada")
    menu = input("Digite novamente:")
print("Saiu")

