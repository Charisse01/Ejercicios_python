# En base al promedio de 8 calificaciones numéricas ingresadas por el profesor, mostrar en pantalla la calificación final en letra del estudiante, tomando en cuenta la siguiente escala:

def calificacion():
    
    for i in range(15):
        numero = int(input('Introduzca la calificacion: '))
        if numero >= 90 and numero <= 100: 
            print("A")
        if numero == 100:
            print("Muchas felicidades")

        if numero >= 80 and numero <= 89: 
            print("B")

        if numero >= 70 and numero <= 79 : 
            print("C")

        if numero >= 60 and numero <= 69 : 
            print("D")

        if numero <= 59: 
            print("F", "Usted esta reprovado")

calificacion()