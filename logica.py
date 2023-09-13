import random

#Función para calcular la unión de dos alfabetos
def union_alfabetos(alfabeto1, alfabeto2):
    return alfabeto1.union(alfabeto2)

#Función para calcular la diferencia de dos alfabetos
def diferencia_alfabetos(alfabeto1, alfabeto2):
    return alfabeto1.difference(alfabeto2)

#Función para calcular la intersección de dos alfabetos
def interseccion_alfabetos(alfabeto1, alfabeto2):
    return alfabeto1.intersection(alfabeto2)

#Función para calcular la cerradura de estrella de un alfabeto
def cerradura_estrella(alfabeto, n):
    palabras_generadas = set()
    for _ in range(n):
        palabra = ''.join(random.choice(list(alfabeto)) for _ in range(random.randint(1, 10)))
        palabras_generadas.add(palabra)
    return palabras_generadas

# Definir una función para calcular la unión de dos lenguajes
def union_lenguajes(lenguaje1, lenguaje2):
    return lenguaje1.union(lenguaje2)

# Definir una función para calcular la diferencia de dos lenguajes
def diferencia_lenguajes(lenguaje1, lenguaje2):
    return lenguaje1.difference(lenguaje2)

# Definir una función para calcular la intersección de dos lenguajes
def interseccion_lenguajes(lenguaje1, lenguaje2):
    return lenguaje1.intersection(lenguaje2)

# Definir una función para calcular la concatenación de dos lenguajes
def concatenacion_lenguajes(lenguaje1, lenguaje2):
    resultado = set()
    for palabra1 in lenguaje1:
        for palabra2 in lenguaje2:
            resultado.add(palabra1 + palabra2)
    return resultado

# Definir una función para calcular la potencia de un lenguaje
def potencia_lenguajes(lenguaje1, lenguaje2, n):
    if n < 0:
        return set()  # Potencia negativa es un conjunto vacío

    resultado1 = set()
    resultado2 = set()
    
    if n == 0:
        resultado1.add('')  # Potencia 0 contiene la cadena vacía
        resultado2.add('')  # Potencia 0 contiene la cadena vacía
    else:
        for _ in range(n):
            nuevo_conjunto1 = set()
            nuevo_conjunto2 = set()
            for cadena1 in resultado1:
                for simbolo in lenguaje1:
                    nuevo_conjunto1.add(cadena1 + simbolo)
            for cadena2 in resultado2:
                for simbolo in lenguaje2:
                    nuevo_conjunto2.add(cadena2 + simbolo)
            resultado1 = nuevo_conjunto1
            resultado2 = nuevo_conjunto2

    return resultado1, resultado2



# Definir una función para calcular la inversa de un lenguaje
def inversa_lenguaje(lenguaje):
    resultado = set()
    for palabra in lenguaje:
        resultado.add(palabra[::-1])
    return resultado

# Definir una función para calcular la cardinalidad de un lenguaje
def cardinalidad_lenguaje(lenguaje1):
    return len(lenguaje1)

# Interfaz de usuario mínima por línea de comandos
if __name__ == "__main__":
    alfabeto1 = set(input("Ingrese el primer alfabeto (separado por comas):\n").split(','))
    alfabeto2 = set(input("Ingrese el segundo alfabeto (separado por comas)\n").split(','))
    print("Unión de alfabetos:\n", union_alfabetos(alfabeto1, alfabeto2))
    print("Diferencia de alfabetos:\n", diferencia_alfabetos(alfabeto1, alfabeto2))
    print("Intersección de alfabetos:\n", interseccion_alfabetos(alfabeto1, alfabeto2))
    
    n_cerradura_estrella = int(input("Ingrese el número de palabras para la cerradura de estrella:\n "))
    print("Cerradura de estrella del alfabeto:\n", cerradura_estrella(alfabeto1, n_cerradura_estrella))

    lenguaje1 = set(input("Ingrese el primer lenguaje:\n "))
    lenguaje2 = set(input("Ingrese el segundo lenguaje:\n "))
    n = set(input("Ingrese el numero de potencia:\n "))

    #lenguajes
    print("Unión de lenguajes:\n", union_lenguajes(lenguaje1, lenguaje2))
    print("Diferencia de lenguajes:\n", diferencia_lenguajes(lenguaje1, lenguaje2))
    print("Intersección de lenguajes:\n", interseccion_lenguajes(lenguaje1, lenguaje2))
    print("concatenación  de lenguajes:\n", concatenacion_lenguajes(lenguaje1, lenguaje2))
    print("Potencia del primer lenguaje:", (lenguaje1, lenguaje2, n))
    print("Potencia del segundo lenguaje:", (lenguaje1, lenguaje2, n))
    print("Inversa de lenguajes:\n", inversa_lenguaje(lenguaje1))
    print("Cardinalidad de lenguajes:\n", cardinalidad_lenguaje(lenguaje1))