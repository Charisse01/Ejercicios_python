# Realizar un programa que rellene una lista de 20 elementos con los números 
# comprendidos entre 20 y 39 y copie en otro array esos números multiplicados por 0.18

lista1 = []
lista2 = []

for x in range(20, 40):
    lista1.append(x)

for i in lista1:
    mult = round(i * 0.18)
    lista2.append(mult)
  


print(lista1)
print(lista2)
 