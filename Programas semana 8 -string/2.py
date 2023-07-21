# Queremos hacer un programa que cuente cuántos hashtags hay en un Tweet. 
# Para lograr eso, tendríamos que recorrer todo el texto, encontrando cada carácter “#” para contarlo. 

tweet = input("Ingresa tu tweet: ")
numero = len(tweet)
x = 0
contador = 0 
while x < len(tweet): 
    
  if tweet[x] == "#":
    contador += 1
  x += 1
print("Escribiste " + str(contador), "Hashtags en total")
