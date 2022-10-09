# %%
import pandas as pd

# %%

minha_serie = [30, 29, 27, 16, 54, 42]

sum(minha_serie)/len(minha_serie)

# %%

minha_serie = pd.Series(minha_serie)

# %%

minha_serie

# %%
minha_serie.mean()

# %%

minha_serie.describe()

# %%
minha_serie # tem índices que são mutáveis

# %%
minha_serie.index = ["a","b", "c", "d","e", "f"]

minha_serie

# %%

print(minha_serie[0])
print(minha_serie['a'])

# %%

minha_serie * 10

