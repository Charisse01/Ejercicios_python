# Realizar un programa que, tras ingresar seis números enteros en un array, 
# determine la posición del array en la que se encuentra el máximo valor.

lista1 = []

for i in range(6):
    numuero = int(input("Ingrese un número: "))
    lista1.append(numuero)
    valormaxi = max(lista1)
    indi = lista1.index(valormaxi)

print(f"\nEl valor máximo es el: {valormaxi} y esta en la posicion: {indi} ")
print()
