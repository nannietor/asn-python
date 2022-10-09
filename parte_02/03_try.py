# %%
try:
    num = int(input("Entre com um número: "))

    if num % 2 == 0:
        print(f'{num} é par')

    else: 
        print(f'{num} é impar')
except ValueError as err:
    print("Entre com a porra de um numero valido")
    print(err)
