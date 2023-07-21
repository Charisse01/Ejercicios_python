#Queremos realizar un programa que regule la cantidad de caracteres que se pueden 
# escribir en una frase, siendo el limite de caracteres 60.

while True:
    text = input("ingrese un texto: ")
    caracteres = len(text)
    if caracteres > 60:
        print("\nEl texto es un poco largo, pruebe con uno más corto")
        print()

    else:
        print("\nEl texto ingresado fue: " + text)
    break



