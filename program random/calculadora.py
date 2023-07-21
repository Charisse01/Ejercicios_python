print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

seleccion = input("Selecciona una operación (1/2/3/4): ")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if seleccion == '1':
    print(num1 + num2)
elif seleccion == '2':
    print(num1 - num2)
elif seleccion == '3':
    print(num1 * num2)
elif seleccion == '4':
    print(num1 / num2)
else:
    print("Entrada inválida")
