def contar_vocales(palabra):
    # Contador de vocales
    contadores = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    
    # Recorrer cada letra de la palabra
    for letra in palabra:
        if letra.lower() in contadores:  # Verificar si la letra es una vocal
            contadores[letra.lower()] += 1
    
    return contadores

# Función para encontrar y contar las vocales en una palabra
def encontrar_vocales(palabra):
    # Llamamos a la función contar_vocales
    resultados = contar_vocales(palabra)
    total_vocales = sum(resultados.values())
    
    # Imprimir los resultados
    print("Vocales encontradas:")
    for vocal, cantidad in resultados.items():
        if cantidad > 0:
            print(f"{vocal} = {cantidad}")
    
    print(f"En total son: {total_vocales} vocales")

# Main
palabra = input("Ingrese una frase: ")
encontrar_vocales(palabra)
