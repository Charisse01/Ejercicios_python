#Realizar un algoritmo para sumar consecutivamente y cuando la suma sea superior a 100 deje de pedir números y muestre el total

suma = 0
numero = int(input("Ingrese un número: "))

while numero != 0:
    suma += numero 
    if (suma > 100):
        break 
    numero = int(input("Ingrese un número: ")) 

print("Suma total:",suma)
    

