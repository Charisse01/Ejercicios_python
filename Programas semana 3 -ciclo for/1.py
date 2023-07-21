# Realizar un algoritmo que muestre los impares que hay entre 1 y un valor introducido por el teclado.

numero1 = 1
numero2 = int(input("ingrese numero: "))

if numero2 < numero1:
    print(f"ingrese un número mayor o igual que {numero1}")
else:
    for i in range(numero1, numero2 + 1):
        if i % 2 == 1 :
             print(f"El número {i} es impar.")
        










