#Elabore un algoritmo que indique si una persona debe de sacar tu cedula de identidad tomando en cuenta previamente que haya ingresado su año de nacimiento. (recordar que la edad mínima para obtener la cedula de identidad es 18 años)

edad = int(input("Ingrese su año de nacimiento: "))

if edad < 2003 and edad > 0:
    print("Usted es mayor de edad")
    print("Debe sacar su cedula")
else:
    print("Todavia es menor de edad ")
 



