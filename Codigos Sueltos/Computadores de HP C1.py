C=int(input("Ingrese la cantidad de computadores que puede transportar en un dia: "))
while C<=0 or C>1000:
    print("Valor fuera de rango")
    C=int(input("Ingrese la cantidad de computadores que puede transportar en un dia: "))
n=int(input("Ingrese la cantidad de dias a evaluar: "))
while n<=0:
    print("Valor fuera de rango")
    n=int(input("Ingrese la cantidad de dias a evaluar: "))
d=1
b=0
while d<=n:
    d=str(d)
    a=int(input("Ingrese la cantidad de computadores que llegaron en el dia "+d+": "))
    while a<=0:
        print("Valor fuera de rango")
        a=int(input("Ingrese la cantidad de computadores que llegaron en el dia "+d+": "))
    d=int(d)
    if a>C:
        b=b+(a-C)
    if a<=C:
        b=b-(C-a)
    if b<0:
        b=0
    b=str(b)
    print("La cantidad de computadores en la bodega es de "+b)
    b=int(b)
    d=d+1
