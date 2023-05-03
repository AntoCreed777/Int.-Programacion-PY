n=int(input("Numero de valores que va a ingresar: "))
while n<=0 or n>100:
    print("Error, valor mal ingresado")
    n=int(input("Numero de valores que va a ingresar: "))
for i in range(n):
    p=int(input("Numero a evaluar: "))
    while p<=0:
        print("Error, valor mal ingresado")
        p=int(input("Numero a evaluar: "))
    i=1
    d=0
    while i!=p:
        if p%i==0:
            d=d+i
        i=i+1
    if d==p:
        p=str(p)
        print(p+" es Perfecto")
    else:
        p=str(p)
        print(p+" No es perfecto")