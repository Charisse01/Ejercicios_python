# Realizar un programa que rellene una lista con los 40 primeros números pares y 
# calcule su suma y promedio.

lista1 = []

for i in range(1, 81):
    if i % 2 == 0:
        lista1.append(i)

cantidad = len(lista1)
suma = sum(lista1)
promedio = suma / cantidad

print(lista1)

print(f"\nLa suma es de los primeros 40 numeros es:  {suma} y el promedio es: {promedio} ")
print()
