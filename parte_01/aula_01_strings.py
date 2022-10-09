# %%
meu_nome = "Natalia Magno"

print(len(meu_nome)) # calcula o número de caracteres da string
# %%
print("Primeira letra: ", meu_nome[0]) # Python começa no índice 0
print("Segunda letra: ", meu_nome[1])
print("Última letra: ", meu_nome[12])

tamanho = len(meu_nome)
print("última letra: ", meu_nome[tamanho-1])
print("última letra: ", meu_nome[-1])

print("penúltima letra: ", meu_nome[-2])
# %%
# Fatiamento (slicing)

print(meu_nome[0:3]) # start:stop - stop vai até a última - 1
# range = stop - start (tamanho que vai retornar)

print(meu_nome[8:11]) # fatiamento no meio

print(meu_nome[0:-1]) # Todas menos a última letra

print(meu_nome[:3]) # As três primeiras

print(meu_nome[-3:]) # As três últimas
# %%
#start,stop,step
#step é o tamanho do passo

print(meu_nome[::2]) # pula de 2 em 2
print(meu_nome[0:3:2]) 
print(meu_nome[::-1]) # inverte a ordem da string
