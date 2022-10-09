# %%

dados = [
    {
        "match_id": 6758406426,
        "duration": 3274,
        "start_time": 1663194074,
        "radiant_team_id": 111474,
        "radiant_name": "Alliance",
        "dire_team_id": 8344760,
        "dire_name": "Team Bald Reborn",
        "leagueid": 14574,
        "league_name": "WEU TI 11 Regional Qualifiers",
        "series_id": 704369,
        "series_type": 1,
        "radiant_score": 18,
        "dire_score": 43,
        "radiant_win": False,
    },
    {
        "match_id": 6758352967,
        "duration": 2674,
        "start_time": 1663189914,
        "radiant_team_id": 111474,
        "radiant_name": "Alliance",
        "dire_team_id": 8344760,
        "dire_name": "Team Bald Reborn",
        "leagueid": 14574,
        "league_name": "WEU TI 11 Regional Qualifiers",
        "series_id": 704369,
        "series_type": 1,
        "radiant_score": 34,
        "dire_score": 24,
        "radiant_win": True,
    },
    {
        "match_id": 6758281133,
        "duration": 2331,
        "start_time": 1663185840,
        "radiant_team_id": 111474,
        "radiant_name": "Alliance",
        "dire_team_id": 8344760,
        "dire_name": "Team Bald Reborn",
        "leagueid": 14574,
        "league_name": "WEU TI 11 Regional Qualifiers",
        "series_id": 704369,
        "series_type": 1,
        "radiant_score": 5,
        "dire_score": 27,
        "radiant_win": False,
    }
]

dados[1]['radiant_name']
# %%
dados[-1]['radiant_name']

# %%
dados[0].keys()

# %%

dados[0].values()

# %%

dados[0].items() # retorna tuplas

# %%

import requests

url = "https://api.opendota.com/api/proMatches"

dados = requests.get(url).json()

# %%
len(dados) # uma lista com 100 dicionários, cada um referente a uma partida

## mongodb armazena documentos chave, valor. ideal para armazenar json

# %%
# dicionários são mutáveis, é possível criar chaves novas
dados[0]['user_name'] = "Teo Calvo"

# %%
dados[0]