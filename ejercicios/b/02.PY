# MAQUINA EXPENDEDORA

GASEOSA = 5.00 #CREAR UNA CONSTANTE

while True:#INICIALIZAR MI CICLO WHILE EN VERDADERO Y SE DETENDRA CON EL BREAK AL FINAL DEL CODIGO
    total_dinero = 0.0  # Inicializa el total de dinero ingresado por el usuario

    while total_dinero < GASEOSA:# MIENTRAS  TOTAL DINERO  SEA MENOR QUE GASEOSA
        dinero = float(input("Ingrese moneda: "))#PEDIMOS EL DINERO
        total_dinero += dinero#SE ACUMULA EN TOTAL DINERO 
        if total_dinero < GASEOSA:#SI EL DINERO ES MENOR GASEOSA 
            print(f"Faltan ${GASEOSA - total_dinero} para completar la compra.")

    if total_dinero == GASEOSA:#SI ES IGUAL
        print("Gracias por su compra.")
    elif total_dinero > GASEOSA:#EL DINERO ES MAYOR QUE GASEOSA 
        vuelto = total_dinero - GASEOSA#VUELTO 
        print(f"Gracias por su compra. Su vuelto es ${vuelto}.")

    opc = input("¿Desea seguir comprando? (S/N): ").strip().upper()#COMO FUNIONA STRIP
    if opc != "S":#ES DISTINTO A ---
        print("¡Hasta luego!")
        break

    