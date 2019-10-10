import csv

input_file = csv.DictReader(open("outputFile.csv"))
studentsList = []

for row in input_file:
    studentsList.append(row)

for student in studentsList:
    print("Nombre: " + student["nombre"])
    print("Edad: " + str(student["edad"]))
    print("Cursos: " + student["cursos"])
