class Persona:

    personas = []

    def __init__(self, name, dni):
        self.name = name
        self.dni = dni
        Persona.personas.append(self)

    def dar_info(self):
        return f'Name: {self.name}\nDNI:{self.dni}'

    @staticmethod
    def contar_personas( ):
        return len(Persona.personas)

a = Persona("Pepito", 32830199)
b = Persona("Jorge", 28555666)
print(a.name)
print(Persona.contar_personas())

