import csv

studentsList = []
studentIn = {'nombre' : 'Juan', 'edad' : 19, 'cursos': ['Basic'] }
studentsList.append(studentIn)
studentIn = {'nombre' : 'Marcos', 'edad' : 20, 'cursos': ['Turbo C','Pascal'] }
studentsList.append(studentIn)

for student in studentsList:
    print("Nombre: " + student["nombre"])
    print("Edad: " + str(student["edad"]))
    print("Cursos: ")
    for curso in student["cursos"]:
        print("  " + curso)


with open("outputFile.csv", "wb") as f:
    w = csv.DictWriter(f, studentsList[0].keys())
    w.writeheader()
    for student in studentsList:
        w.writerow(student)

