import time 

nombre = input("¿como te llamas?: ")
print("Hola, "+ nombre, "Es hora de jugar al ahorcado")
print(" ")
time.sleep(1)
print("Comienza a adivinar")
time.sleep(0.5)
palabra= "azumaquina"
tupalabra= ''
vidas= 5

while vidas > 0:

    fallas= 0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end= "")
        else:
            print("*", end= " ")
            fallas += 1
    if fallas == 0:
        print("\nFelicidadades Ganaste!!")
        break

    tuletra= input("\nIntroduce una letra: ")
    tupalabra += tuletra

    if tuletra not in palabra:
        vidas -= 1
        print("Te equivocaste")
        print("Tu tienes", +vidas, "vidas")
    if vidas == 0:
        print("perdiste :(")
else:
    print("gracias por participar")