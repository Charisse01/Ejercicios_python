# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de 
# ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje 
# informando de ello.

dic = {'Platano':1.35, 'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}

frutas= input("Introduzca la fruta requerida: ").title()
costo= float(input("Ingrese cuantas quiere llevar: "))

if frutas in dic:
    print(round(costo), 'kilos de', frutas, 'cuestan', round(dic[frutas]*costo), 'Pesos')
else: 
    print(dic.get(frutas.title(), "Lo siento pero esta fruta no se encuentra"))