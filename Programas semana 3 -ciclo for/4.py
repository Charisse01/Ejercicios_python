#Un algoritmo que permita ingresar N datos correspondientes al género de N, número de personas y determine el porcentaje de hombres y mujeres que hay.

h = []
m = []

for i in range(15):
    genero = input("Ingrese el genero h/m: ")
    if genero == 'h':
        h.append(genero)
    if genero == 'm':
        m.append(genero)    
    contar1 = len(h)
    contar2 = len(m)
    suma = contar1 + contar2

    porcentaje1 = (contar1 * 100)/suma
    porcentaje2 = (contar2 * 100)/suma
print(f"el porcentaje de mujeres es:{porcentaje1} ")
print(f"el porcentaje de hombres es:{porcentaje2} ")












