# %%
# exercício 1.2
nome = input('Qual é o seu nome?')
print('Olá ', nome,'! Seja bem vindo!', sep="")
# %%
# exercício 1.2
nome = input('Qual é o seu nome?')
idade = input('Qual é a sua idade?')
print(f'Olá {nome},bom saber que você tem {idade} anos. Seja bem vindo!') # utilizando placeholder
# %%
# exercício 1.3
raio = float(input('Qual é o raio da circunferência?'))
pi = 3.14
perimetro = round(2*pi*raio,2)
area = round(pi * (raio**2),2)
print('Área =', area)
print('Perímetro = ', perimetro)
# %%
# exercício 1.4
a = int(input('Qual é o primeiro valor a ser somado?'))
b = int(input('Qual é o segundo valor a ser somado?'))
print('Soma dos valores: ', a+b)
# %%
# exercício 1.5
a = float(input('Qual é o primeiro valor?'))
b = float(input('Qual é o segundo valor?'))
print(f"Potência dos valores {a:.2f} ^ {b:.2f} {a**b:.2f}")


#Atalhos VsCode:
#seleciona as linhas que quer editar ao mesmo tempo e digita shift+alt+i para selecionar várias linhas
#end vai pro final da linha
#seleciona duas letras e digita ctrl_shift_p (procura por upper ou lower)
#se ficar apertando alt e selecionar linhas, dá pra escrever em varias linhas
#se selecionar uma palavra e clicar ctrl+d ele vai selecionando todas as palavras iguais, se escrever algo em cima substitui