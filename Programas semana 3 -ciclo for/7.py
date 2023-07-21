#Elabora un algoritmo que solicite la edad de 20 personas y que muestre cuantos son mayores y menores de edad

mayores = []
menores = []

for i in range(20):
    edad = int(input("Ingrese una edad: "))
    if edad >= 18:
        mayores.append(edad)
    else:
        menores.append(edad)
    contar1 = len(mayores)
    contar2 = len(menores)

print(f"Hay {contar1} mayores y {contar2} menores")

    
 