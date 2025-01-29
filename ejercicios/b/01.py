#calculadora hasta ingresar salir


print("****1.SUMA***")
print("****2.RESTA**")
print("**3.MULTIPLI*")
print("****4.SALIR***")

def suma(a, b):
    resultado = a + b
    return resultado

def resta(a, b):
    resultado = a - b
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    return resultado

while True:
        opc = int(input("Ingrese opción: "))
        if opc == 4:
            print("Saliendo...")
            break
        
        num1 = int(input("Ingrese número 1: "))
        num2 = int(input("Ingrese número 2: "))

        if opc == 1:
            print(f"Resultado de la suma: {suma(num1, num2)}")
        elif opc == 2:
            print(f"Resultado de la resta: {resta(num1, num2)}")
        elif opc == 3:
            print(f"Resultado de la multiplicación: {multiplicacion(num1, num2)}")
        else:
            print("Opción no válida, intente nuevamente.")
    
