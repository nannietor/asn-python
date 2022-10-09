# %%

# Exercício 1.6

notas = []

for i in range(1,5):
    nota = float(input("Entre com a nota {i}: "))
    notas.append(nota)

media = sum(notas)/len(notas)
menor = min(notas)
maior = max(notas)

print("Média:", media)
print("Menor:", menor)
print("Maior:", maior)

# %%

# Exercício 2.4

def eh_primo(x):
    for i in range(2,x):
        if x % i == 0:
            return False

    return True # tá fora do for

numero = int(input("Entre com um número: "))

if eh_primo(numero):
    print(f"O numero {numero} é primo")
else:
    print(f"O número {numero} não é primo")
# %%

# Fibonacci

def fib(pos):
    fib_seq = [0,1]

    while True:
        if len(fib_seq)-1>= pos:
            return fib_seq[pos]
        else:
            fib_seq.append(fib_seq[-1]+fib_seq[-2])

numero = int(input("Entre com uma posição da Seq Fib: "))
print(fib(numero))

# %%

# Outra Opção


def fib(pos):
    fib_seq = [0,1]

    while True:

        try:
            return fib_seq[pos]
        except IndexError:
            fib_seq.append(fib_seq[-1]+fib_seq[-2])

numero = int(input("Entre com uma posição da Seq Fib: "))
print(fib(numero))

# %%

# Exercício 2.6

frase = "Esta é a frase original"

frase_lista = frase.split()
frase_nova = ""
for palavra in frase_lista:
    frase_nova += palavra[::-1] + " "

print(frase_nova)

# %%

for i in range(1,101):
    texto =""
    if i % 3 == 0:
        texto += "Fizz"
    if i % 5 == 0:
        texto += "Buzz"
    
    if texto == "":
        print(i)
    else:
        print(texto)

# %%

def fat(x):
    res = 1
    for i in range(2,x+1):
        res *= i


# %%

import random

N = 670
n = 5
album = set([])
counter = 0
while len(album) < N:
    pacote = [random.randint(1,N) for i in range(n)]
    album.update(set(pacote))
    counter +=1

counter

# %%

def compra_pacote(N=670, n=5):
    pacote = set([random.randint(1,N) for i in range(n)])
    return pacote

def preenche_album(N=670, n=5):
    album = set()
    count = 0
    while len(album) < N:
        pacote = compra_pacote(N,n)
        album.update(pacote)
        count += 1

    return count

N=670
n = 5

ite = 10000

pacotinhos=[preenche_album(N,n) for i in range(ite)]
pacotinhos

# %%
import matplotlib.pyplot as plt

plt.hist(pacotinhos)
plt.grid(True)
plt.title("Pacotes para completar album")
plt.show()
