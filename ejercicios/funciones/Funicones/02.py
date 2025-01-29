
# Lista de números romanos del 1 al 10
lista = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


# Función que convierte el número a romano
def romanos(num):
    # Verificar si el número está dentro del rango de 1 a 10
    if 1 <= num <= 10:
        print(f"El número ingresado es {num}, el número convertido a romano es {lista[num - 1]}")
    else:
        print("Número fuera de rango. Ingrese un número entre 1 y 10.")

# Main principal
num = int(input("Ingrese un número entre 1 y 10: "))
romanos(num)

