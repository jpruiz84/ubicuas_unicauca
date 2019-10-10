import time
import csv

userList = []

input_file = csv.DictReader(open("usuarios.csv"))

for row in input_file:
    userList.append(row)


print("Registros previos: " + str(len(userList)))

inTimeLast = time.time()
while True:
    user = {}

    user["nombres"] = raw_input("Introduzca los Nombres del usuario, 'fin' para terminar: ")
    if user["nombres"].upper() == "fin".upper():
        break

    user["apellidos"] = raw_input("Introduzca los Apellidos del usuario: ")
    user["edad"] = raw_input("Introduzca la edad del usuario: ")
    user["tiempoDeRegistro"] = time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(time.time()))

    if time.time() - inTimeLast > 20:
        break

    inTimeLast = time.time()
    userList.append(user)

with open('usuarios.csv', 'wb') as f:
    w = csv.DictWriter(f, userList[0].keys())
    w.writeheader()
    for user in userList:
        w.writerow(user)
