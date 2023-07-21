import random

lower = "abcdefghijklmnñopqrstuvwxyz"
upper = lower.upper()
numeros = "0123456789"

x = lower + upper
y = upper + numeros 
z = lower + numeros
all = lower + upper + numeros 

mayusculas = input("¿Desea tener mayusculas en la contraseña? (Y/N): ")   
minusculas = input("¿Desea tener minusculas en la contraseña? (Y/N): ")
nums = input("¿Desea tener numeros en la contraseña? (Y/N): ")
caracteresTotal = int(input("¿De cuanto caracteres quiere la contraseña?: "))

if mayusculas == 'Y' and minusculas == 'N' and nums == 'N':       # solo mayusculas 
    contraseña = "".join(random.sample(upper, caracteresTotal))  
    print(f"\nLa contraseña es: {contraseña}" )

if mayusculas == 'Y' and minusculas == 'Y' and nums == 'N':      # solo mayusculas y minusculas
    contraseña = "".join(random.sample(x, caracteresTotal))
    print(f"\nLa contraseña es: {contraseña}" )

if mayusculas == 'Y' and minusculas == 'N' and nums == 'Y':      # solo mayusculas y numeros 
    contraseña = "".join(random.sample(y, caracteresTotal))
    print(f"\nLa contraseña es: {contraseña}" )
    
if mayusculas == 'N' and minusculas == 'N' and nums == 'Y':       # solo numeros  
    contraseña = "".join(random.sample(numeros, caracteresTotal))
    print(f"\nLa contraseña es: {contraseña}" )

if mayusculas == 'N' and minusculas == 'Y' and nums == 'N':         # solo minusculas 
    contraseña = "".join(random.sample(lower, caracteresTotal))
    print(f"\nLa contraseña es: {contraseña}" )

if mayusculas == 'N' and minusculas == 'Y' and nums == 'Y':         # solo minusculas y numeros 
    contraseña = "".join(random.sample(z, caracteresTotal))
    print(f"\nLa contraseña es: {contraseña}" )

if mayusculas == 'Y' and minusculas == 'Y' and nums == 'Y':            # todas 
    contraseña = "".join(random.sample(all, caracteresTotal))
    print(f"\nLa contraseña es: {contraseña}" )

if mayusculas == 'N' and minusculas == 'N' and nums == 'N':            # Nada
    print("\n\033[91m {}\033[00m" .format("Ok no quiere nada, No lo ejecute entonces :)"))
    print()

