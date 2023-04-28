n=int(input("Ingrese numero de pelotas: "))
while n<=0:
    print("Error, numero fuera de rango")
    n=int(input("Ingrese numero de pelotas: "))
s=1
m=101
while n!=0:
    r=int(input("Ingrese el tamaño de las pelotas: "))
    while r<=0:
        print("Error, numero fuera de rango")
        r=int(input("Ingrese el tamaño de las pelotas: "))
    if m==r:
        s=s+1
    if m>r:
       m=r
       s=1
    n=n-1

s=str(s)
m=str(m)

print("Se han producido "+s+" pelotas de radio "+m)