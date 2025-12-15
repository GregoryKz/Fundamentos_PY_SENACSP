cliente = {"nome":"Pascoal", "numero": 11959474132, "idade": 25, "cpf": "12345678933", "endereço": "rua tito" }
print(cliente)
print(len(cliente))
print(cliente["endereço"])
del cliente["nome"]
print(cliente)
print(len(cliente))
cliente["nome"] = "Gregory"
print(cliente)
print(len(cliente))