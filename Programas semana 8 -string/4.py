# Haz un programa que reciba un string y lo imprima carácter por carácter
def imprimir_string(s):
  for x in s:
    print(x)

def imprimir_string2(s):
  for i in range(len(s)):
    print(s[i])

def imprimir_string3(s):
  countador = 0
  while countador < len(s):
    print(s[countador])
    countador += 1

s = input("Ingrese su string: ")
imprimir_string(s)
print("--------------------")
imprimir_string2(s)
print("--------------------")
imprimir_string3(s)
print("--------------------")
