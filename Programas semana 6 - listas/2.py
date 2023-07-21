# Realizar un programa que rellene una lista con los números pares comprendidos 
# entre 1 y 20

lista = []

for x in range(1, 21):
    if x % 2 == 0:
        lista.append(x)

print(lista)