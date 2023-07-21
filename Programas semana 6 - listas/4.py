# Realizar un programa que rellene una lista con 10 números enteros consecutivos 
# y haga una copia de ese array en otro

lista1 = []

for x in range(1, 11):
    lista1.append(x)

lista2 = lista1
print(lista1)
print(lista2)
