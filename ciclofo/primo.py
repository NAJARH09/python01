n = int(input("Ingrese numero: "))
contador = 0

# Revisamos desde 1 hasta n (excluyendo 0 para evitar división por cero)
for x in range(1, n + 1):
    if n % x == 0:  # Si `n` es divisible por `x`
        contador += 1

# Un número primo tiene exactamente 2 divisores: 1 y él mismo
if contador == 2:
    print("Primo")
else:
    print("NO es primo")
