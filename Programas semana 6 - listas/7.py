# Realizar un programa que solicite diez números, los almacene en un array y luego 
# calcule el promedio de esos números

lista1 = []

for i in range(10):
    numuero = int(input("Ingrese un número: "))
    lista1.append(numuero)

suma = sum(lista1)
cantidad = len(lista1)
promedio = round(suma / cantidad)

print(f"\nEl promedio de estos números es: {promedio} ")
print()
