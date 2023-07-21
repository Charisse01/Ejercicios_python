# Escribir un programa que cree un diccionario simulando una cesta de la compra. El 
# programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que 
# el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y 
# el coste total, con el siguiente formato

compras = {}
continuar = True
while continuar:
    arct = input("Introduzca un artículo: ")
    precio = float(input('Introduce el precio del ' + arct + ': '))
    compras[arct] = precio
    print(compras)
    continuar = input('¿Quieres añadir más información (s/n)? ') == "s"
costo = 0
print('Lista de lo que compro: ')
for arct, precio in compras.items():
    print(arct, round(precio))
    costo += round(precio)
print(f'El total de la compra es: {costo} pesos')

