# Haz una función que reciba un string y dos índices. Se debe retornar el string que va entre 
# las posiciones indicadas por los índices. Si las posiciones no son validas se debe avisar.

def sstring(s, x, y):
    if x > 0 and y < len(s) and x < y:
        return s[x:y]
    else:
        print("indices no validos")
        return ""

s = input("Ingrese su string: ")
x = int(input("Indice x: "))
y = int(input("Indice y: "))
print(sstring(s, x, y))
