#repasando
numero=[1,2,3,4,5]
print(numero)

priPosi=numero[0]
lon=len(numero)
print(f'primer valor es :{priPosi}\nLa longitud es {lon}')
for num in numero:
    print(num)
    
    
#apartado 2
#sublistas e indexeado--A>cceder 
#indices negatavios
lista=["damaris","yomira","lilia"]
ultiPosi=lista[-1]
print(ultiPosi)

#sublistas
sub=lista[1:3]
print(sub)

#sublista
slista=lista[:3]
print(slista)


#apartado 3
edad=[12,13,14,32]

#comprobar si elelemento pertenece a la lista:
palabra1=12
palabra2=6
if palabra1 in lista:
    print("Si pertence")

if palabra2 not in lista:
    print("no esta en la lista")


#apartado 4 :modificar elementos

semana=["lunes","martes","miercoles","jueves","viernes"]

semana[1]="domingo"

#apartado 5 :metodo de las litas
#añadir elementos
#ejemplo    variableDeTipoLista.metodo()

nom=["maru","luci","carlos"]
print(nom)
nom.insert(2,"Damaris")
print(nom)

#añadir al final de la lista
nom.append("yomira")
print(nom)
#apartado 6



#ejercicio