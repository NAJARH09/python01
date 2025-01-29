num1=int(input("Ingresa número 1 :"))
num2=int (input("Ingresa número 2 :"))
num3=int(input("Ingresa número 3 :"))



if num1>num2:
    m=num1
else:
    m=num2
    if num3>m:
        m=num3
        

print(m)