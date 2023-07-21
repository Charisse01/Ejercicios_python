# Realizar mediante el uso de diccionarios un tablero de tres en raya parece un gran hachís
#símbolo (#) con nueve ranuras que pueden cada contener una X, una O o un espacio en blanco. 
#epresentar el tablero con un diccionario, puedes asigne a cada ranura una clave de valor de 
#cadena,

import os
# Tic - tac - toe

# Pizarra
# En este diccionario se almacena la pizarra donde se van colocando los valores
# Las posiciones estan a la izquierda (llave) y los valores a la derecha (valor)
# En este caso la prizarra esta vacia ya que a medida que se va jugando se va llenando
laPizarra = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
}

# ---------- FUNCIONES ---------- #
# Imprimir los valores del diccionario
def imprimirPizarra(pizarra):
    print(pizarra['top-L'] + '|' + pizarra['top-M'] + '|' + pizarra['top-R'])
    print('-+-+-')
    print(pizarra['mid-L'] + '|' + pizarra['mid-M'] + '|' + pizarra['mid-R'])
    print('-+-+-')
    print(pizarra['low-L'] + '|' + pizarra['low-M'] + '|' + pizarra['low-R'])

# Llenar datos en el diccionario
def juego():
    turn = 'X'
    # Este ciclo se va a ejecutar 9 veces ya que solo hay 9 posibles jugadas antes de que se tranque el juego
    for i in range(9):
        imprimirPizarra(laPizarra)
        print(f'turno de juego para {turn} selecciona un espacio')
        movimiento = input('Ingresa movimiento de ' + turn + '-> ')

        # Verifica que no se mande una posicion vacia
        while movimiento == '':
            print('Debes igresar una posicion')
            movimiento = input('Ingresa movimiento de ' + turn + '-> ')
        valido = movValido(movimiento)

        # Verifica que la posicion sea valida
        while valido:
            print('Movimiento invalido!!')
            movimiento = input('Ingresa movimiento de ' + turn + '-> ')

            if not movValido(movimiento):
                break

        # Aqui se le asigna el valor al diccionario en la posicion indicada
        laPizarra[movimiento] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        # Esto limpia la consola
        os.system('clear')
        
        # Verifica si gano la X o el O
        if ganadorX():
            print('Gano la X!!')
            break
        elif ganadorO():
            print('Gano el O!!')
            break

    
    imprimirPizarra(laPizarra)

# Verifica si gano la X
def ganadorX():
    # Ganador vertical
    if laPizarra['top-L'] == 'X' and laPizarra['mid-L'] == 'X' and laPizarra['low-L'] == 'X':
        return True
    elif laPizarra['top-M'] == 'X' and laPizarra['mid-M'] == 'X' and laPizarra['low-M'] == 'X':
        return True
    elif laPizarra['top-R'] == 'X' and laPizarra['mid-R'] == 'X' and laPizarra['low-R'] == 'X':
        return True

    # Ganador horizontal
    if laPizarra['top-L'] == 'X' and laPizarra['top-M'] == 'X' and laPizarra['top-R'] == 'X':
        return True
    elif laPizarra['mid-L'] == 'X' and laPizarra['mid-M'] == 'X' and laPizarra['mid-R'] == 'X':
        return True
    elif laPizarra['low-L'] == 'X' and laPizarra['low-M'] == 'X' and laPizarra['low-R'] == 'X':
        return True

    # Ganador diagonal
    if laPizarra['top-L'] == 'X' and laPizarra['mid-M'] == 'X' and laPizarra['low-R'] == 'X':
        return True
    elif laPizarra['low-L'] == 'X' and laPizarra['mid-M'] == 'X' and laPizarra['top-R'] == 'X':
        return True

    return False

# Verifica si gano el O
def ganadorO():
    # Ganador vertical
    if laPizarra['top-L'] == 'O' and laPizarra['mid-L'] == 'O' and laPizarra['low-L'] == 'O':
        return True
    elif laPizarra['top-M'] == 'O' and laPizarra['mid-M'] == 'O' and laPizarra['low-M'] == 'O':
        return True
    elif laPizarra['top-R'] == 'O' and laPizarra['mid-R'] == 'O' and laPizarra['low-R'] == 'O':
        return True

    # Ganador horizontal
    if laPizarra['top-L'] == 'O' and laPizarra['top-M'] == 'O' and laPizarra['top-R'] == 'O':
        return True
    elif laPizarra['mid-L'] == 'O' and laPizarra['mid-M'] == 'O' and laPizarra['mid-R'] == 'O':
        return True
    elif laPizarra['low-L'] == 'O' and laPizarra['low-M'] == 'O' and laPizarra['low-R'] == 'O':
        return True

    # Ganador diagonal
    if laPizarra['top-L'] == 'O' and laPizarra['mid-M'] == 'O' and laPizarra['low-R'] == 'O':
        return True
    elif laPizarra['low-L'] == 'O' and laPizarra['mid-M'] == 'O' and laPizarra['top-R'] == 'O':
        return True

    return False

# Verifica si el movimiento que se va hacer es valido
def movValido(movimiento):
    # Estas condiciones comprueban que el movimiento ingresado por el usuario sea valido
    if movimiento == 'top-L' or movimiento == 'top-M' or movimiento == 'top-R':

        if laPizarra[movimiento] == 'X':
            return True
        elif laPizarra[movimiento] == 'O':
            return True

        return False
    elif movimiento == 'mid-L' or movimiento == 'mid-M' or movimiento == 'mid-R':

        if laPizarra[movimiento] == 'X':
            return True
        elif laPizarra[movimiento] == 'O':
            return True

        return False
    elif movimiento == 'low-L' or movimiento == 'low-M' or movimiento == 'low-R':

        if laPizarra[movimiento] == 'X':
            return True
        elif laPizarra[movimiento] == 'O':
            return True

        return False
    else:
        return True
# ---------- FUNCIONES ---------- #

juego()
