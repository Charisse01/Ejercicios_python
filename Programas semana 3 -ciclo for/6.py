# Elabora un algoritmo que permita mostrar el sueldo promedio de un grupo de empleados.

for i in range(6):
    sueldos = int(input("Ingrese el sueldo diario: "))
    promedio = round(sueldos * 365 / 12)
    print(f"Su sueldo promedio es: {promedio} $")