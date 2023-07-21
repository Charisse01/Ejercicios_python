#Hacer un programa que imprima la suma de los 100 primeros números.

numeros = []

for x in range(1, 100 + 1):
    numeros.append(x)
    suma = sum(numeros)
print(f"La suma de los primeros 100 numeros es: {suma}")


