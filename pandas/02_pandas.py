# %%
import pandas as pd

# %%

df_dict = {'nome': ['Teo','Nah', 'Maria'],
      'idade': [30, 32, 1],
      'sexo': ["M", "F", "F"]
      }

df_dict
    
# %%
df = pd.DataFrame(df_dict)
df

# %%
# acessar coluna

df['nome']

# %%

df_dict['nome']

# %%

type(df['nome'])

# %%

df.describe() 

# %%

df['nome'].describe()

# %%

# data frame é representado por um conjunto de séries



