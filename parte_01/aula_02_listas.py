# %%
# A lista é um conjunto de objetos (qualquer tipo de objeto e misturados)
# Array tem que ser os mesmos tipos
valores = [30, 32, 0.999, 35]
valores
# %%
sum(valores) / len(valores)

# %%
# interators
 # strings
 # listas
 # range
 # tupla
 # dict

# %%

dados_teo = ["Teodoro", 
             30, 
            "Head of Data",
            ["Maria", "Marcela", "Josefina"]]

dados_teo[3][-1][0]

# %%

dados_teo.append("UNESP - Estatística")
# aqui ele realmente modifica o objeto (pois lista é mutável)
dados_teo

# %%
dados_teo.append(["Fox", "Maria"])

dados_teo

# %%

dados_teo.remove(["Fox", "Maria"])
dados_teo

# %%
# %%

dados_teo.remove('UNESP - Estatística',)
dados_teo

# %%
dados_teo.extend(["Fox", "Maria"])
dados_teo

# %%
dados_teo += ["Gamers Club", "Natalia"]
dados_teo

# %%
dados_teo = dados_teo[:2] + dados_teo[-2:]
dados_teo


# %%
meu_dict = {"chave": "valor"}
meu_dict

# %%

meu_dict = {
    "nome": "Téo",
    "idade": 30,
    "carro": "Fox",
    "ex": ["Maria", "Angelica", "Marcela"],
    "empresas": ["Gamers Club", "Via Varejo", "GB"],
    "skills": [
        {"nome": "python", "nivel": "expert"},
        {"nome": "sql", "nivel": "inter"},
        {"nome": "estatística", "nivel": "iniciante"}
    ]
}

meu_dict['empresas']