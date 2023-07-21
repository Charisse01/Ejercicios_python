#Leer la edad de 20 personas, determinando cuántas de las edades están en el intervalo de 18 a 90.

edad1 = []

for i in range(20):
    edad2 = int(input("Ingrese la edad: "))
    if edad2 >= 18 and edad2 <= 90:
        edad1.append(edad2)
        contar = len(edad1)
print(f"Hay {contar} edades que estan enel intervalo de 18 a 90")

    
    








    

      
    



