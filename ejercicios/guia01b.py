estatura = float(raw_input("Introduzca su estatura (metros): "))
peso = float(raw_input("Introduzca su peso (kilos): "))

imc = peso/(estatura*estatura)

print("Su imc es: " + str(imc))
