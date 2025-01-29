#saber si es un palindromo sin funciones

print("Ingrese una palabra")
palabra = input().strip()
i = 0
j = len(palabra) - 1
esPali = True

while  i<j and esPali:
    if palabra[i] != palabra[j]:
        esPali=False
    i=i+1
    j-=1

if esPali:
    print(f'Es un palindromo')
else:
    print(f'No es palindromo')
    