

def contagem ():
    for i in range(11):
        print(i)

def contagem_2():
    for i in range(0,11,2):
        print(i)
contagem_2()        

alunos = ["Gregory", "Lucas"]
def boaNoite():
    for i in alunos:
        print(f"Boa noite {i}")

print("="*15)        
contagem()
print("="*15)
contagem_2()
print("="*15)
boaNoite()