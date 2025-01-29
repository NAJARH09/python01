#numero primo
def Primo(num):
    contador = 0  # Inicializamos el contador de divisores
    
    for i in range(1, num + 1):  # Iterar desde 1 hasta num (inclusive)
        if num % i == 0:  # Si num es divisible por i
            contador += 1  # Incrementamos el contador
    
    # Verificar si el número es primo
    if contador == 2:  # Un número primo tiene exactamente dos divisores (1 y él mismo)
        print("Es primo")
    else:
        print("No es primo")

# Main


# Main
while True:
    num = int(input("Ingrese un número mayor o igual a 1: "))
    Primo(num)
    opc = input("Ingrese 'x' para salir o 'a' para seguir: ").strip().lower()  # Limpiamos espacios y convertimos a minúsculas
    if opc == 'x':  # Comparamos correctamente como cadena
        print("Saliendo del programa. ¡Hasta luego!")
        break
    
     
    

