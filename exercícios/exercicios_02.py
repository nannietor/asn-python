# %%
# exercício 1.7
lista =  [120, "Python", 120.01, "asn", False, [10,20]]

print("Elemento -1: ", lista[-1])
print("Primeiro elemento: ", lista[0])
print("Último caracter do segundo elemento: ", lista[1][-1]

# %%
# exercício 1.8
numero = int(input("Digite o número em segundos: "))
#60s = 1 min
#360s = 60 min = 1 h

horas= numero//(60 * 60)
segundos = numero % (60*60)

minutos= segundos // 60
segundos = segundos % 60

texto = f'{horas:0>2}:{minutos:0>2}:{segundos:0>2}'
print(texto)
