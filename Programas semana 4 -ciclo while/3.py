#Realizar un algoritmo que pida al usuario digitar un color y lo muestre, pero cuando el usuario digita el color rojo se termine y lo indica.

color1 = "rojo"
color2 = input("Ingrese un color: ")
print(color2)

while color2 != color1:
    color2 = input("Ingrese un color: ")
    print(color2)
    if color2 == color1:
        break

