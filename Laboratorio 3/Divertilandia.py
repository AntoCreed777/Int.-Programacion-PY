n=int(input("Numero de integrantes de la familia: "))
while n<=0:
    print("Error, valor mal ingresado")
    n=int(input("Numero de integrantes de la familia: "))
i=1
p=0
while i<=n:
    e=int(input("Edad del integrante: "))
    while e<=0:
        print("Error, valor mal ingresado")
        e=int(input("Edad del integrante: "))
    if e<=18 and e>=4:
        p=p+5000
    if e>18 and e<65:
        p=p+10000
    if e>=65:
        p=p+3000
    i=i+1
p=str(p)
print("Debe pagar $"+p)