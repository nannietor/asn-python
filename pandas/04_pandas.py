# %%

import pandas as pd

# %%
path = r'C:\Users\natal\OneDrive\Documents\asn_rocks\asn_python\pandas\data\order_items.csv'
df = pd.read_csv (path)

df.head()

# %%

df.info(memory_usage='deep')

# %%

df.info()

# %%

df.dtypes #é uma série, o nome das colunas são os índices

# %%

type(df.dtypes)

# %%

df.dtypes.index.tolist()

# %%

df.describe()
#df.describe(include='all') # é um dataframe

# %%

df['vlPrice'][4] # df[column][index]

# %%
prices = ['vlPrice','vlFreight']
df[prices]

# %%
df[['vlPrice','vlFreight']]

# retorna um data frame, então não dá pra
# selecionar uma linha com [0], por exemplo.
# tem que usar iloc

# %%

df[['vlPrice','vlFreight']].iloc[0]

# %%

df.loc[0] # retorna a linha 3, ou seja, índice 3
# tem que passar o índice da linha
# Acessa a linha do data frame pelo índice

# %%

type(df.loc[0])

# %%

#Acessar a linha do dataframe pela ordem da linha

df.iloc[35] # posição da linha

# %%

# Acessar coluna: pelo nome da coluna
# Se pegar uma coluna só, eu tenho uma série. Então posso selecionar
# linha pelo índice ex. [0], .loc (índice) ou .iloc (ordem)
# Se pegar duas colunas, retorna um dataframe. Daí, ele primeiro espera
# que vc selecione uma coluna, então não funciona o [0], apenas o .iloc e .loc.

# %%

bool_menor_1 = df['vlPrice'] < 1
bool_menor_1

# retorna série de booleanos

# %%

df[bool_menor_1]


# %%

A = [1,2,3]
B = A

B[2] = 'Téo'

print('B:',B)
print('A:',A)

# modifica nos dois dataframes pq na verdade ele tá olhando o mesmo objeto,
# que está com dois 'post its' A e B.
# Para isso n acontecer, tenho q usar .copy


# %%

A = [1,2,3]
B = A.copy()

B[2] = 'Téo'

print('B:',B)
print('A:',A)

# %%

# SEMPRE COPIAR OS DADOS!!

# MAS CUIDADO Q VAI ONERAR A MEMÓRIA, SE FOR NECESSÁRIO APAGAR O ORIGINAL
# del A (desreferencia um objeto)