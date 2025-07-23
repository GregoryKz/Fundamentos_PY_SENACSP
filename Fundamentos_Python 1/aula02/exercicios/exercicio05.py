# 1=Branco
# 2=verde
# 3=vermelho

print('Vamos votar em um time (1-Branco), (2-Verde) e (3-Vermelho)')
nome = input("Digite seu nome:")
voto = int(input('Digite qual e seu time:'))
if (voto==1):
    print(f'{nome} votou branco')
elif (voto==2):
    print (f'{nome} votou verde')
elif (voto== 3):
    print (f'{nome} votou no vermelho')
else:
    print('Voto errado')    
print('Obrigado pelo seu voto!')