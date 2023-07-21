
import os
# Juego Tic - tac - toe

# Tablero
# En este diccionario que se creo se almacenará el tablero donde se van colocando los valores

elTablero = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
}


def imprimirPizarra(tablero):
    print(tablero['top-L'] + '|' + tablero['top-M'] + '|' + tablero['top-R'])
    print('-+-+-')
    print(tablero['mid-L'] + '|' + tablero['mid-M'] + '|' + tablero['mid-R'])
    print('-+-+-')
    print(tablero['low-L'] + '|' + tablero['low-M'] + '|' + tablero['low-R'])

# Llenar datos en el diccionario
def partida():
    turno = 'X'
    # Este ciclo se va a ejecutar 9 veces ya que solo hay 9 posibles jugadas antes de que se tranque el juego
    for i in range(9):
        imprimirPizarra(elTablero)
        print(f'Es el turno para que juegue la {turno} selecciona un espacio')
        movimiento = input('Ingresa movimiento de ' + turno + '-> ')

        # Verifica que no se mande una posicion vacia
        while movimiento == '':
            print('Debes igresar una posicion')
            movimiento = input('\nIngresa movimiento de ' + turno + '-> ')
        valido = movValido(movimiento)

        # Verifica que la posicion sea valida
        while valido:
            print('Movimiento invalido!!')
            movimiento = input('\nIngresa movimiento de ' + turno + '-> ')

            if not movValido(movimiento):
                break

        # Aqui se le asigna el valor al diccionario en la posicion indicada
        elTablero[movimiento] = turno
        if turno == 'X':
            turno = 'O'
        else:
            turno = 'X'

        
        # Verifica si gano la X o el O
        if ganadorX():
            print('\nGanó la X, FELICIDADES!')
            break
        elif ganadorO():
            print('\nGanó el O, FELICIDADES!')
            break

    
    imprimirPizarra(elTablero)

# Verifica si gano la X
def ganadorX():
    # Ganador vertical
    if elTablero['top-L'] == 'X' and elTablero['mid-L'] == 'X' and elTablero['low-L'] == 'X':
        return True
    elif elTablero['top-M'] == 'X' and elTablero['mid-M'] == 'X' and elTablero['low-M'] == 'X':
        return True
    elif elTablero['top-R'] == 'X' and elTablero['mid-R'] == 'X' and elTablero['low-R'] == 'X':
        return True

    # Ganador horizontal
    if elTablero['top-L'] == 'X' and elTablero['top-M'] == 'X' and elTablero['top-R'] == 'X':
        return True
    elif elTablero['mid-L'] == 'X' and elTablero['mid-M'] == 'X' and elTablero['mid-R'] == 'X':
        return True
    elif elTablero['low-L'] == 'X' and elTablero['low-M'] == 'X' and elTablero['low-R'] == 'X':
        return True

    # Ganador diagonal
    if elTablero['top-L'] == 'X' and elTablero['mid-M'] == 'X' and elTablero['low-R'] == 'X':
        return True
    elif elTablero['low-L'] == 'X' and elTablero['mid-M'] == 'X' and elTablero['top-R'] == 'X':
        return True

    return False

# Verifica si gano el O
def ganadorO():
    # Ganador vertical
    if elTablero['top-L'] == 'O' and elTablero['mid-L'] == 'O' and elTablero['low-L'] == 'O':
        return True
    elif elTablero['top-M'] == 'O' and elTablero['mid-M'] == 'O' and elTablero['low-M'] == 'O':
        return True
    elif elTablero['top-R'] == 'O' and elTablero['mid-R'] == 'O' and elTablero['low-R'] == 'O':
        return True

    # Ganador horizontal
    if elTablero['top-L'] == 'O' and elTablero['top-M'] == 'O' and elTablero['top-R'] == 'O':
        return True
    elif elTablero['mid-L'] == 'O' and elTablero['mid-M'] == 'O' and elTablero['mid-R'] == 'O':
        return True
    elif elTablero['low-L'] == 'O' and elTablero['low-M'] == 'O' and elTablero['low-R'] == 'O':
        return True

    # Ganador diagonal
    if elTablero['top-L'] == 'O' and elTablero['mid-M'] == 'O' and elTablero['low-R'] == 'O':
        return True
    elif elTablero['low-L'] == 'O' and elTablero['mid-M'] == 'O' and elTablero['top-R'] == 'O':
        return True

    return False

# Verifica si el movimiento que se va hacer es valido
def movValido(movimiento):
    # Estas condiciones verifican que el movimiento ingresado por el usuario sea valido
    if movimiento == 'top-L' or movimiento == 'top-M' or movimiento == 'top-R':

        if elTablero[movimiento] == 'X':
            return True
        elif elTablero[movimiento] == 'O':
            return True

        return False
    elif movimiento == 'mid-L' or movimiento == 'mid-M' or movimiento == 'mid-R':

        if elTablero[movimiento] == 'X':
            return True
        elif elTablero[movimiento] == 'O':
            return True

        return False
    elif movimiento == 'low-L' or movimiento == 'low-M' or movimiento == 'low-R':

        if elTablero[movimiento] == 'X':
            return True
        elif elTablero[movimiento] == 'O':
            return True

        return False
    else:
        return True

partida()
