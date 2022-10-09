# %%

import requests
import pandas as pd

# %%

url = "https://api.opendota.com/api/proPlayers"

resposta = requests.get(url)

# %%
resposta.content

# %%
data = resposta.json()

data

# %%
data[0]

# %%

df = pd.DataFrame(data)
df

# %%
df.to_csv('dados_dota.csv', index = False)