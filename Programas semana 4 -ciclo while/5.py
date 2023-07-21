# Modificar el programa anterior para que el mismo incluya tres partidos políticos, al final debe de imprimir los siguientes datos:

validos = 0
nulos = 0
pld = 0
prm = 0
prd = 0


cantidadDeVotos = int(input("Introduzca la cantidad de votos: "))
limiteDeVotos = 0

while limiteDeVotos < cantidadDeVotos:
    edad = int(input("\nIntroduce tu edad: "))
    nacionalidad = input("Introduce tu nacionalidad: ")
    partido = input("Introduce tu partido politico: ")
    limiteDeVotos = limiteDeVotos + 1

    if edad >= 18 and nacionalidad == "dominicana" and partido == "pld":
        validos = validos + 1
        pld = pld + 1
        # print("La cantidad de votos validos es igual:", validos)

    elif edad >= 18 and nacionalidad == "dominicana" and partido == "prm":
        validos = validos + 1
        prm = prm + 1

    elif edad >= 18 and nacionalidad == "dominicana" and partido == "prd":
        validos = validos + 1
        prd = prd + 1

    else:
        nulos = nulos + 1
        # print("La cantidad de votos nulos es igual:", nulos)

print("\nLa cantidad de votos del pld es:", pld)
print("\nLa cantidad de votos del prm es:", prm)
print("\nLa cantidad de votos del prd es:", prd)
print("\nLa cantidad de votos validos es igual:", validos)
print("La cantidad de votos nulos es igual:", nulos)