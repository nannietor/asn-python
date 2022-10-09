# %%
print("Olá mundo!")
# %%
nome = "Nat"
print(nome)
# %%
nome = input("Entre com o seu nome: ")
print("Seu nome é: ", nome)
# %%
# "# %%" cria um bloco, como se fosse no jupyter
# %%
texto_longo = '''
Esse é
um
texto
longo 
viu
'''
print(texto_longo)
# %%
print("1+1 = ",1+1)
# %%
print("10 - 231= ",10-231)
print("10*2 = ", 10*2)
print("4/3 = ", 4/3)
print("10 % 3 = ", 4 % 3) #resto
print("10 // 3 = ", 10 // 3) #parte inteira da divisão
print("10 ** 2 = ", 10**2) #exponenciação
print("4**(1/2) = ", 4**(1/2)) #raiz quadrada não tem nativamente no python
print("True = ", True)
print("False = ", False)
print("True + True ", True + True)
# %%
raio = 1 # definiu o raio
pi = 3.14 # definiu o pi
area = pi * (raio ** 2) # calculou a área

print("Área =", area)
# %%
idade_1 = int(input("Idade pessoa1: "))
idade_2 = int(input("Idade pessoa2: "))

media = (idade_1 + idade_2) / 2
print("Média de idade: ", media)