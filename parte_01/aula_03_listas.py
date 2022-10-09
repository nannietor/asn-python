# %%
# descompressão de listas
from ast import NodeTransformer


x = [1.5,2.7] # notas

#n1 = x[0]
#n2 = x[1]

# fazendo a descompressão
n1, n2 = x
print(n1)

# %%

x = [1.5, 2.7, 7.6]
# não quero o terceiro elemento

n1, n2, *_ = x # ele vai desconsiderar todo o resto (o underline é só a boa prática, pode ser qualquer coisa, exemplo *n)

n1, *_, n2 = x # pega o primeiro, o último e desconsidera todo do meio
# %%
a = 10
b = 20 
# mas quero que a = 20 e b = 10

a, b = b, a # descompressão de tuplas

print(a, b)