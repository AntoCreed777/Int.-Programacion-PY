k=int(input("Ingrese autos por minutos: "))
while k<=0:
    print("Error, numero fuera de rango")
    k=int(input("Ingrese un numero: "))
n=int(input("Ingrese cantidad de minutos: "))
while k<=0:
    print("Error, numero fuera de rango")
    n=int(input("Ingrese cantidad de minutos: "))

s=0
p=k*n

while n!=0:
    a=int(input("Ingrese cantidad de autos: "))
    while a<=0:
        print("Error, numero fuera de rango")
        a=int(input("Ingrese cantidad de autos: "))
    s=s+a
    n=n-1
if s>p:
    r=s-p
else:
    r=0
print(r)