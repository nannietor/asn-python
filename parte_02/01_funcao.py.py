# %%
def f(x): # assinatura da função (parâmetros que ela recebe)
    # corpo da função
    resultado = 2 * (x**2) - 6 * x + 125
    return resultado

print( f(1) )

# identação -> 4 espaços por convenção

# %%

def g(x=0): # argumento opcional
    return 2 * x + 10

print(g())

# %%

def soma(a,b=0):
    return a + b

print(soma(10))

# %%

# como documentar a função?

def concat(nome, sobrenome=""):
    ''' # Docstring
    Essa função concatena um nome com um sobrenome,
    utilizando um espaço entre as palavras.
    Os argumentos necessários para essa função, são:
        nome: string
        sobrenome: string
    '''
    return f'{nome} {sobrenome}'.title()

print(concat("natalia"))

# %%
help(concat)

# %%

# Para utilizar a função em outros programas,
# é preciso tê-la em um programa e importá-la.
# Exemplo: from arquivo import nome_função

# %%
def concat(nome:str, sobrenome="")->str:
    # como definimos o sobrenome como string, já aparece na hint
    # nome:str é para dar a hint pro usuário, não obriga ele a inputar uma string
    ''' # Docstring
    Essa função concatena um nome com um sobrenome,
    utilizando um espaço entre as palavras.
    Os argumentos necessários para essa função, são:
        nome: string
        sobrenome: string
    '''
    return f'{nome} {sobrenome}'.title()

print(concat("teo"))

# %%

# %%
def soma(*args, ignore_even=False): # não precisa definir os argumentos
    return sum(args)

print(soma(20,30,47,95, ignore_even=True))

# %%

# kwargs - dicionário
# args - lista

def config(teclado, mouse, **kwargs):
    print("Teclado:",teclado)
    print("Mouse:", mouse)
    print(kwargs)

config('Logitech', 'Logitech', headset='Corsair', monitor='LG')

# %%
query='''
select {fodase}
from {tb_nao_sei}
where date > {date}
'''

def format_query(query,**kwargs):
    return query.format(**kwargs)

print(format_query(query, fodase='teste', tb_nao_sei = 'fodase', date='2022-06-02'))