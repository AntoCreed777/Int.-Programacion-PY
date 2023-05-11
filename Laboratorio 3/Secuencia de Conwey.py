n=int(input("Numero de salidas: "))
while n<=0 or n>20:
    print("Error, valor mal ingresado")
    n=int(input("Numero de salidas: "))
v=int(input("Valor a procesar: "))
while v<0 or v>=10:
    print("Error, valor mal ingresado")
    v=int(input("Valor a procesar: "))
x=1
y=1
c=1
g=0
p=1
z=1
print(v)
while x<n:
    a=v%10
    if y==1:
        b=a
    else:
        if a==b:
            c=c+1
        else:
            g=g+c*(10**p)+b*(10**(p-1))
            b=a
            c=1
            p=p+2
    y=y+1
    v=v//10
    if v==0:
        if z!=1:
            print(g)
            y=1
            p=1
            v=g
            g=0
            z=1
            x=x+1
        else:
            z=z+1