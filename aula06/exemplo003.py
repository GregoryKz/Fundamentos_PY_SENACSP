import matplotlib.pyplot as plt


categorias = ['Python', 'Java', 'JavaScript', 'HTML5', 'CSS3']
quantidade = [80,65,40,69,71]

plt.bar(categorias,quantidade)
plt.title("Linguagens mais famosas ")
plt.xlabel("Linguagens")
plt.ylabel("Quantidade")

plt.show()
