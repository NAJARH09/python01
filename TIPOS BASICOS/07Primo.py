numero = int(input("Ingrese número: "))
contador = 0

for x in range(1, numero + 1):  # Iterar desde 1 hasta el número inclusive
    if numero % x == 0:  # Verificar divisibilidad
        contador += 1  # Incrementar contador

if contador == 2:  # Si solo tiene dos divisores, es primo
    print("Es un número primo")
else:
    print("No es primo")
