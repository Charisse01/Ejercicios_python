# Realizar un programa que tras asignar 10 valores enteros en un array, determine 
# las posiciones del array en las que se encuentran el máximo y el mínimo valor

lista1 = []

for i in range(10):
    numuero = int(input("Ingrese un número: "))
    lista1.append(numuero)
    valormaxi = max(lista1)
    indi = lista1.index(valormaxi)

    valormin = min(lista1)
    indi1 = lista1.index(valormin)


print(f"\nEl valor máximo es el: {valormaxi} y esta en la posicion: {indi} ")
print(f"\nEl valor minimo es el: {valormin} y esta en la posicion: {indi1} ")

print()
