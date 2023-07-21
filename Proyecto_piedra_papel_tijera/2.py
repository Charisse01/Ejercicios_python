import random

aleatorio = random.randrange(0, 3)

elijePc = ""
elijeUsuario = ""

print("\033[91m {}\033[00m" .format("--- Menu de opciones: ---"))
print("1 )Piedra")
print("2) Papel")
print("3) Tijera")
print("4) Lagarto")
print("5) Spock")
print()
opcion = int(input("\033[92m {}\033[00m" .format("Cual elijes: ")))
print()


if opcion == 1:
    elijeUsuario = "piedra"
elif opcion == 2:
    elijeUsuario = "papel"
elif opcion == 3:
    elijeUsuario = "tijera"
elif opcion == 4:
    elijeUsuario = "lagarto"
elif opcion == 5:
    elijeUsuario = "spock"

     

print("Tu: ", elijeUsuario)

if aleatorio == 0:
    elijePc = "piedra"
elif aleatorio == 1:
    elijePc = "papel"
elif aleatorio == 2:
    elijePc = "tijera"
elif aleatorio == 3:
    elijePc = "lagarto"
elif aleatorio == 4:
    elijePc = "spock"

print("Contrincante: ", elijePc)
print()

if elijePc == "papel" and elijeUsuario == "tijera":
    print("Ganaste, tijera corta papel")

elif elijePc == "piedra" and elijeUsuario == "papel":
    print("Ganaste, papel tapa a piedra")

elif elijePc == "lagarto" and elijeUsuario == "piedra":
    print("Ganaste, Piedra aplasta a lagarto")

elif elijePc == "spock" and elijeUsuario == "lagarto":
    print("Ganaste, lagarto envenena a spock")

elif elijePc == "tijera" and elijeUsuario == "spock":
    print("Ganaste, spock rompe a tijera")

elif elijePc == "lagarto" and elijeUsuario == "tijera":
    print("Ganaste, tijera decapita a lagarto")

elif elijePc == "papel" and elijeUsuario == "lagarto":
    print("Ganaste, lagarto devora a papel")

elif elijePc == "spock" and elijeUsuario == "papel":
    print("Ganaste, papel deasutoriza a spock")

elif elijePc == "piedra" and elijeUsuario == "spock":
    print("Ganaste, spock vaporiza a piedra")

elif elijePc == "tijera" and elijeUsuario == "piedra":
    print("Ganaste, piedra aplasta a tijera")


if elijePc == "tijera" and elijeUsuario == "papel":
    print("perdiste, tijera corta a papel")

elif elijePc == "papel" and elijeUsuario == "piedra":
    print("perdiste, papel tapa a piedra")

elif elijePc == "piedra" and elijeUsuario == "lagarto":
    print("perdiste, Piedra aplasta a lagarto")

elif elijePc == "lagarto" and elijeUsuario == "spock":
    print("perdiste, lagarto envenena a spock")

elif elijePc == "spock" and elijeUsuario == "tijera":
    print("perdiste, spock rompe a tijera")

elif elijePc == "tijera" and elijeUsuario == "lagarto":
    print("perdiste, tijera decapita a lagarto")

elif elijePc == "lagarto" and elijeUsuario == "papel":
    print("perdiste, lagarto devora a papel")

elif elijePc == "papel" and elijeUsuario == "spock":
    print("perdiste, papel desautoriza a spock")

elif elijePc == "spock" and elijeUsuario == "piedra":
    print("perdiste, spock vaporiza a piedra")

elif elijePc == "piedra" and elijeUsuario == "tijera":
    print("perdiste, piedra aplasta a tijera")

elif elijePc == elijeUsuario:
    print("empate")
print()
