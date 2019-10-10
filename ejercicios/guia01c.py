import time

userList = []
userInputTime = []

inTimeLast = time.time()
while True:
    user = raw_input("Introduzca el usuario, 'fin' para terminar: ")
    if user.upper() == "fin".upper():
        break
    if time.time() - inTimeLast > 5:
        break

    inTimeLast = time.time()
    userList.append(user)
    userInputTime.append(time.time())


count = 0
for user in userList:
    print(str(count) + ". " + user + ", fecha de registro: " + \
        time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(userInputTime[count])))
    count += 1
