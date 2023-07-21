# Realizar un algoritmo que simule el funcionamiento de la alarma de un reloj digital permitiendo que el usuario 
# indique en que hora deberá parar el reloj, mostrando el transcurrir del tiempo en pantalla y al final un mensaje de alerta.

import time

repeticion = 0
aprobar = True

def tiempo(h, mn, s):
    while aprobar: 
        if (h == time.strftime('%H')) and (mn == time.strftime('%M')) and (s == time.strftime('%S')):
            for i in range(repeticion):
                time.sleep(1)
            print("!!Es hora de despiertar!!")
            break
        print(time.strftime("%H: %M: %S"))

h = input('Ingrese la hora (HH24): ')
mn = input('Ingrese los minutos (MM): ')
s = input('Ingrese los segundos (SS): ')
    
tiempo(h, mn, s)
        
        
        





