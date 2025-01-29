# Función para saludar
def saludar(nombre):
    print(f"Hola {nombre}")

# Función para calcular la edad
def calcularAño(fecha):
    resultado = 2024 - int(fecha)  # Restar el año actual menos el año de nacimiento
    return resultado  # Devolver el resultado

# Llamadas a las funciones
nombre = input("Ingresa tu nombre: ")
saludar(nombre)

fecha = int(input("Ingresa tu año de nacimiento: "))
edad = calcularAño(fecha)  # Llamada a calcularAño y almacenar el resultado
print(f"Tienes {edad} años.")
