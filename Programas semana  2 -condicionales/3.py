#En un curso de matemáticas la calificación final del estudiante se determina a partir del siguiente esquema:

calificacion1 = int(input("Ingrese la calificacion final de las pacticas : "))
calificacion2 = int(input("Ingrese la calificacion final de las tareas : "))
calificacion3 = int(input("Ingrese la calificacion final del proyecto final : "))
calificacion4 = int(input("Ingrese la calificacion del examen final: "))

Promedio1 = calificacion1 * 35 / 100
Promedio2 = calificacion2 * 25 / 100 
Promedio3 = calificacion3 * 20 / 100
promedio4 = calificacion4 * 20 / 100

notaFinal = (Promedio1 + Promedio2 + Promedio3 + promedio4)

print(f"Su calificación final es; {notaFinal}")


