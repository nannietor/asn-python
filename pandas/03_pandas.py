# %%

import pandas as pd

# %%


df = pd.read_csv(r'C:\Users\natal\OneDrive\Documents\asn_rocks\asn_python\pandas\data\order_items.csv')

df

# %%

df.head(20) # cabeçalho 

# %%

df.tail() # cauda

# %%

df.shape # tupla

# %%

df.columns # traz nome das colunas

# %%

type(df.columns)

# %%

df.columns.to_list() # converte pra lista

# %%

df.index