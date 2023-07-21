# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo 
# guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene 
# <edad> años, vive en <dirección> y su número de teléfono es <teléfono>


for i in range(1):
    nom= input("ingrese nombre: ")
    ed= input("ingrese su edad: : ")
    tell= input("ingrese su numero de telefono: ")
    direc= input("ingrese la dirección donde vive: ")

print(f"\nSu nombre es: {nom}, Tiene: {ed} años, Vive en: {direc}, y su número de telefono es: {tell}")
print()