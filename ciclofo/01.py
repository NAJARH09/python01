for i in range (0,11):
    n=int(input("Ingrese numero"))
    if i==0:
        mayor=n
    elif n>mayor:
        mayor=n
    else:
       print("error")
       
print(mayor)