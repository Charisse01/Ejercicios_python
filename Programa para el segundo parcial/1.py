# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista 
# y la muestre por pantalla.


asignaturas = []

for i in range(5):
    asig= input("ingrese las asignaturas: ")
    asignaturas.append(asig)

print(asignaturas)