def es_palindromo(texto):
    texto = texto.lower()  # Convertir el texto a minúsculas para hacerlo insensible a mayúsculas/minúsculas
    lista = list(texto)  # Convertir el texto en una lista de caracteres
    lista.reverse()  # Invertir la lista de caracteres
    texto_invertido = ''.join(lista)  # Convertir la lista invertida nuevamente a una cadena
    if texto == texto_invertido:  # Compara el texto original con el texto invertido
        print("Es palíndromo")
    else:
        print("No es palíndromo")

# Prueba de la función
texto = input("Ingresa un texto: ")
es_palindromo(texto)
