# Clase 7

"""
Practica Python
"""

"""
Ejercicio 1
Crear un método para el promedio y la suma
"""

print("Ejercicio 1")


def suma(*numeros):
    resul = 0
    for x in numeros:
        resul += x
    return resul

def promedio(*numeros):
    resul = 0
    contador = 0
    for x in numeros:
        resul += x
        contador +=1
    prom = resul / contador
    return prom

print(promedio(4, 2, 6, 10))

print("\n")

"""
Ejercicio 2
Iterar a través de un array y que muestre el promedio de los datos (mínimo 10 elementos)
"""
print("Ejercicio 2")
print("\n")
array_tres = [8, 4, 3, 7, 1, 9, 5, 2, 6, 10]

resul = 0
contador = 0
for x in array_tres:
        resul += x
        contador += 1
        prom = resul / contador
        print(prom)

print("\n")

"""
Ejercicio 3
Iterar a través de un diccionario con un for para imprimir un texto con ambos valores (Mínimo 5 elementos)
"""
dic_uno = {"pregunta": "¿Cuanto cuesta?", "respuesta": "cien pesos", "cantidad": "llevo dos", "gracias": "De nada",
           "Saludo": "Adiós"}
print("Ejercicio 3")
print("\n")

for k in dic_uno.keys():
    print(k)

for v in dic_uno.values():
    print(v)
print("\n")

"""
Ejercicio 4
Realizar un while que agregue un carácter o un elemento a alguna variable, hasta que supere un largo de 8 elementos
(empezar de algo vacío). Imprimir cada iteración
"""

print("Ejercicio 4")
print("\n")
array_uno = []
print("Cantidad de elementos iniciales: " + str(len(array_uno)))

while len(array_uno) < 9:
    array_uno.append("Algo")
    print(array_uno)

print("Cantidad de elementos finales: " + str(len(array_uno)))