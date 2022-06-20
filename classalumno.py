class Alumno:

    alumnos = []


    def __init__(self, nombre, nota):
        self.name = nombre
        self.nota = nota
        Alumno.alumnos.append(self)

a = Alumno("Jorge", [1, 2, 3, 4, 5])
b = Alumno("Silvana", [6, 7, 8, 9, 10])
print(a.name, a.nota)
print(b.name, b.nota)

Alumno.alumnos[0] = Alumno("Jorge", [1, 2, 3, 4, 5])


