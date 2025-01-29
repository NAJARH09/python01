#lista para traducir al numero romano

romano=["I","II","III","IV","V","VI","VII","VIII","IX","X"]


#FUNCIOPN 
def encontrar(palabra):
    print(f"El número ingresado es {palabra}, el número convertido a romano es {romano[palabra- 1]}")
#main
palabra=int(input("ingrese numero:"))
encontrar(palabra)


