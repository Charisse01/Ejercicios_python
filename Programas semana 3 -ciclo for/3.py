# Realizar un algoritmo que solicite un número y luego genere su tabla de multiplicar desde el 1 hasta el 10

numero= int(input("ingrese un numero: "))

for i in range(1, 11):
    print(numero, "x", i, "=", i * numero)
