n=int(input("Numero de datos que va a ingresar :"))
while n<=0:
    print("Error, valor mal ingresado")
    n=int(input("Numero de datos que va a ingresar :"))

s=0
m=1

for i in range(n):
    a=int(input("Ingrese un Valor"))
    if (a//2)==(a/2):
        s=s+a
    else:
        m=m*a
s=str(s)
m=str(m)

print("La suma de los numeros ingresados es "+s +" y la multiplicacion de los numeros ingresados es "+m )