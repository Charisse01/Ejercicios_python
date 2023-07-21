#
palabra = ''
palabraencriptada = ''
palabradesencriptada = ''

ord = 0

def encriptadas(letras):
    if letras == 'a' or letras == 'A':
        return '15'
    elif letras == 'e' or letras == 'E':
        return '14'
    elif letras == 'i' or letras == 'I':
        return '13'
    elif letras == 'o'or letras == 'O':
        return '12'
    elif letras == 'u' or letras == 'U':
        return '11'
    else:
        return letras

def desencriptadas(numeros):
    if numeros == '15':
        return 'a'
    elif numeros =='14':
        return 'e'
    elif numeros == '13':
        return 'i'
    elif numeros =='12':
        return 'o'
    elif numeros == '11':
        return'u'
    else:
        return numeros

while True:
    print("---Menu de seleccion---")
    print(''' 
        1- Ingresar Frase
        2- Encriptar Frase
        3- Desencriptar Frase
        4- Salir del sistemas 
        ''')
    selecc = int(input("Elige un numero del menu: "))

    if selecc == 1:
        palabra = input("ingresar la frase:  ")
        palabra = palabra.lower()

        letras=0
        for i in palabra:
            if i == 'a':
                letras +=1
            elif i == 'e':
                letras += 1
            elif i == 'i':
                letras += 1
            elif i == 'o':
                letras += 1
            elif i == 'u':
                letras += 1
        if letras == 0:
            palabra=""
            print("Debe tener mas de 4 caracteres")
            palabra = ""

    elif selecc == 2:
        palabraencriptada = ""
        if palabra == "":
            print("Debe ingresar una frase")
        for i in palabra:
            palabraencriptada += encriptadas(i)
        print(palabraencriptada)
    elif selecc == 3:
        if palabra == "":
            print("no se encuentra una frase para desencriptar")
        for i in palabraencriptada:
            if i == "5":
                palabradesencriptada += desencriptadas(i)
            elif i == "4":
                palabradesencriptada += desencriptadas(i)
            elif i == "3":
                palabradesencriptada += desencriptadas(i)
            elif i == "2":
                palabradesencriptada += desencriptadas(i)
            elif i == "1" and ord == 1:
                ord=0
                palabradesencriptada += desencriptadas(i)
            elif i =="1":
                ord += 1
                continue
            else:
                ord = 0
                palabradesencriptada += desencriptadas(i)
    elif selecc == 4:
        break
