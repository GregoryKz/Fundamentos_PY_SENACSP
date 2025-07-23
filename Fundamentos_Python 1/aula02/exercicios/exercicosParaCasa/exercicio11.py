#pode dirigir

podeDirigir = (input("Você pode dirigir (Sim) ou (Não):"))
idade = int(input("Digite sua idade:"))

if (idade>=18 and podeDirigir == "Sim"):
    print ("Liberado")
else:
    print("Volte ano que vem")