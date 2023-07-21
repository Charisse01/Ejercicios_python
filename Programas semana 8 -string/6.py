# Realizar una función que reciba datos tipo string e imprima su valor en la tabla ascii

def numeros_ascii(s):
  for i in s:
    print(ord(i))

s = input("Ingrese string: ")
numeros_ascii(s)
