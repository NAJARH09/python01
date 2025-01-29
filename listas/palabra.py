texto = '''
Un caballo viejo fue vendido para darle vueltas a la piedra de un molino.
Al verse atado a la piedra, exclamó sollozando: - ¡Después de las vueltas
de las carreras, he aquí a que vueltas me he reducido! Moraleja:
No presumáis de la fortaleza de la juventud. Para muchos,
la vejez es un trabajo muy penoso.
'''

por_encontrar = (
    'caballo', 'en', 'aeroplano', 'hola'
)
resultado = [coincidencia for coincidencia in por_encontrar if coincidencia in por_encontrar]

print(f'se ecnotraron las siguientes palabras {resultado}')