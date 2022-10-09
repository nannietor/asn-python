# %%
fruta = 'Banana mAçã'
print(fruta)

#Método é uma ação. Vai aparecer um dropdown quando colocar o .
# O método é invocado junto com o ()
# Métodos são funções definidas dentro do próprio objetos
# %%
fruta.upper() # não altera o próprio objeto, retorna uma cópia
# ele faz isso porque strings no python são imutáveis.
# %%
fruta.lower() # posso fazer fruta = fruta.lower()
#inplace não funciona com string (e é próprio do pandas)
# %%
fruta.lower().endswith('maçã')

# %%
fruta.title() # primeira letra de cada palavra em caixa alta

# %%
fruta.capitalize() # Só primeira letra da sentença fica maiúscula

# %%
fruta.replace("a", "o")

# %%
carro = " carro: Ford Ká "
carro.strip(" .csv")

# %%
#\n faz quebra de linha
print("natalia\nmagno")
# %%
carro.lstrip(" ")
# %%
carro.rstrip(" ")