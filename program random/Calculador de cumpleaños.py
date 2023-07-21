
import datetime

current_date = datetime.date.today().strftime('%Y-%m-%d')

current_date_lst = current_date.split('-')
b_date = input('introduzca su fecha de nacimiento en formato yyyy-mm-dd: ')
print()
name = input('Escria su nombre: ')
print()
b_date = b_date.split('-')

if current_date_lst[1] == b_date[1] and current_date_lst[2] == b_date[2]:
    age = int(current_date_lst[0]) - int(b_date[0])
    print(f"Hoy {name} cumpe {age} años, FELICIDADES!!!")

else:
    print("Lo siento pero hoy no es tu cumpleaños")
print()