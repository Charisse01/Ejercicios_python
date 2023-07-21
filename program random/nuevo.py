

from string import punctuation
def validador_contrasenia(password):
    if len(password)< 8 or len(password) > 14:
        print("La contrasena ha de tener entre 8 y 14 caracteres")
    elif not any([c.isdigit() for c in password]):
        print("La contrasena ha de contener algun digito")
    elif not any([c.islower() for c in password]):
        print("La contrasena ha de contener alguna minuscula")
    elif not any([c.isupper() for c in password]):
        print("La contrasena ha de contener alguna mayuscula")
    elif not any([True if c in punctuation else False for c in password]):
        print("La contrasena ha de contener algun caracter especial")
    else:
        print("Contrasena establecida correctamente")
        return True
    return False

intentos=0

while True:
    contrasenia=input("Introduce contrasena:")
    intentos+=1
    if validador_contrasenia(contrasenia):
        print("La contrasena introducida ha sido {}".format(contrasenia))
        break
    elif intentos>5:
        contrasenia=None
        print("No ha sido posible establecer una contrasena")
        break