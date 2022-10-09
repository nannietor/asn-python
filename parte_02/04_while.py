# %%

x = 1
while x <= 10:
    print(x)
    # x = x + 1
    x += 1
print("Acabou!")

# %%

num = 1
while True:
    print("Foda-se")

    if num==2:
        print("Parando o laço...")
        break

    num += 1

print("Parou!")

# %%

num=0
while True:

    num += 1
    print(f"Foda-se {num}")

    if num % 2 == 0:
        continue

    print("Isso só é para ímpares!")

    if num == 5:
        print("Parando o laço...")
        break
    
print("Parou!")

# %%

# estrutura: while else

num=0
while True:

    num += 1
    print(f"Foda-se {num}")

    if num % 2 == 0:
        continue

    print("Isso só é para ímpares!")

    if num == 5:
        print("Parando o laço...")
        break
else:
    print("Parou! Com sucesso")

