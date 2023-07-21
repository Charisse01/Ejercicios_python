# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
# sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el 
# contenido del diccionario.

dic = {}
continuar = True
while continuar:
    dato = input('¿Qué dato quieres introducir? ')
    x = input(dato + ': ')
    dic[dato] = x
    print(dic)
    continuar = input('\n¿Quieres añadir más información (s/n)? ') == "s"
    print(dic)