
# Crear lista vacía para almacenar las edades
"""edades = []

# Inicializar variables
suma = 0

# Capturar las edades mediante un ciclo for
for i in range(4):
    edad = int(input(f"Ingrese la edad {i + 1}: "))  # Cambié 'edades' por 'edad' para claridad
    edades.append(edad)  # Añadir la edad a la lista


# Calcular el promedio
promedio = suma / 4
print(f"Promedio de edades es {promedio}")
print(f"La edad más baja es {bajo}")

"""
# Crear lista vacía para almacenar las edades
edades = []

# Inicializar variables
suma = 0

# Capturar las edades mediante un ciclo for
for i in range(4):
    edad = int(input(f"Ingrese la edad {i + 1}: "))
    edades.append(edad)
    suma += edad

# Inicializar la edad más baja y más alta con la primera edad ingresada
bajo = edades[0]
alto = edades[0]

# Comparar las edades para encontrar la más baja y la más alta
for edad in edades:
    if edad < bajo:
        bajo = edad
    if edad > alto:
        alto = edad

# Calcular el promedio
promedio = suma / 4

print(f"Promedio de edades es {promedio}")
print(f"La edad más baja es {bajo}")
print(f"La edad más alta es {alto}")
