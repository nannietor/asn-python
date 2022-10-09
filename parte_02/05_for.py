# %%

palavra = 'banana'

for letra in palavra:
    print(letra)

# %%
meu_nome = "Natalia Magno"
meus_dados = [30, 'Nat', 'Bruno', ['Joao', 'Felipe']]

# %%

for i in range(1,11):
    print(i)

# %%

list(range(1,11))

# %%

for i in range(1,11):
    if i % 2 == 0:
        print(f'{i} é par')
    else:
        print(f'{i} é impar')

    if i == 9:
        break
else:
    print("Acabou o range!")

# %%
x = []
for i in range(1,101):
    x.append(i**2)

print(x)

# %%

x = [ i**2 for i in range(1,101)]
x

# %%

for i in range(1,101):
    if i % 3 != 0:
        x.append(i**2)

print(x)

# %%
# é mais rápido do que o jeito anterior

x = [ i**2 for i in range(1,101) if i % 3 != 0]
x