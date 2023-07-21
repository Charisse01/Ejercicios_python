# Realizar un algoritmo que controle que para que una persona pueda ejercer 
#su voto en una elección de gobierno, debe de ser mayor de edad y debe 
#ser dominicana (en caso de no cumplir esta condición se cuenta como 
#voto nulo). Nota: (Cabe destacar que este programa solo permite realizar 
#la cantidad de votaciones que indique el usuario). Al final debe de imprimir 
#la cantidad de votos validos y nulos que se registraron.


validos = 0
nulos = 0

cantidadDeVotos = int(input("Introduzca la cantidad de votos: "))
limiteDeVotos = 0

while limiteDeVotos < cantidadDeVotos:
    edad = int(input("\nIntroduce tu edad: "))
    nacionalidad = input("Introduce tu nacionalidad: ")
    limiteDeVotos = limiteDeVotos +1 

    if edad >= 18 and nacionalidad == "dominicana":
        validos = validos + 1
        # print("La cantidad de votos validos es igual:", validos)
    else:
        nulos = nulos + 1
        # print("La cantidad de votos nulos es igual:", nulos)

print("\nLa cantidad de votos validos es igual:", validos)
print("La cantidad de votos nulos es igual:", nulos)



