# Promedio de ISIL
print("****************************")
print("********ISIL****************")
print("EP:")

# Crear lista para almacenar las notas
notas = []
suma = 0

# Capturar las notas con un ciclo for
for i in range(2):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)  # Agregar nota a la lista
    suma += nota        # Acumular la suma

# Calcular el promedio
promedio = suma / 4

# Capturar parcial y final
parcial = float(input("Ingrese parcial: "))
final = float(input("Ingrese final: "))

# Calcular el EP
ep = (promedio * 0.40) + (parcial * 0.30) + (final * 0.30)

# Mostrar resultado
print(f"El promedio es: {promedio:.2f}")

