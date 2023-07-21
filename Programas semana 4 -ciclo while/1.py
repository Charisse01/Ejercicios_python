# Un algoritmo que permita ingresar N datos correspondientes al género de N, número de personas y determine el porcentaje de hombres y mujeres que hay.

contador = 0
hombres = 0
mujeres = 0

while contador < 7:
    genero = input("Ingrese el genero (M) para masculino y (F) para feminino: ")
    contador = contador + 1

    if genero == "f":
        mujeres = mujeres + 1
    else:
        hombres = hombres + 1 
        

print("\nEl porcentaje de mujeres es: ", mujeres / contador,"%")
print("El porcentaje de hombres es: ", hombres / contador,"%")