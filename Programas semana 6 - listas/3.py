# Realizar un programa que rellene una lista con los números comprendidos entre 
# 75 y 100 divididos por 2

     
lista1 = []
lista2= []

for x in range(75, 101):
    lista1.append(x)

for i in lista1:
    mult = round(i / 2)
    lista2.append(mult)
  


print(lista1)
print(lista2)