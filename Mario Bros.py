n=int(input("Ingrese el numero de murallas: "))

while n<=0 or n>50:
    print("Numero fuera de rango")
    n=int(input("Ingrese el numero de murallas: "))
m=int(1)
r=int(0)
b=int(0)
p=int(0)

while m<=n:
    a=int(input("Ingrese la altura de las murallas: "))
    while a<=0 or a>10:
        print("Numero fuera de rango")
        a=int(input("Ingrese la altura de las murallas: "))
    if p!=0:
        if a>p:
            r=r+1
        if a<p:
            b=b+1
    p=a
    m=m+1

r=str(r)
b=str(b)
print("Saltos hacia arriba: "+r+", Saltos hacia abajo: "+b+".")
