# Realizar un programa que, tras asignar los números, -3, 6, 7, -8, 11, 16 y -3 a un 
# array calcule independientemente la suma de los elementos positivos y negativos
# de manera separada.

lista1 = [-3, 6, 7, -8, 11, 16, -3]

positivos = list(filter(lambda x: x >= 0, lista1))
suma1 = sum(positivos)


negativos = list(filter(lambda x: x <= 0, lista1))
suma2 = sum(negativos)

print(f"\nLos positivos son: {positivos} y la suma de los positivos es: {suma1}")

print(f"\nlos negativos son: {negativos} y la suma de los negativos es: {suma2}")

print()
