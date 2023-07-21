import random

lower = "abcdefghijklmnñopqrstuvwxyz"
upper = lower.upper()
numeros = "0123456789"
simbolos = "[]{}()*;/_-"

all = lower + upper + numeros + simbolos

length = 15
contraseña = "".join(random.sample(all, length))
print(f"\nLa contraseña es: {contraseña}" )
print()
