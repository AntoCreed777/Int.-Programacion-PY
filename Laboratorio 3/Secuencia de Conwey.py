n=int(input("Numero de salidas: "))
while n<=0 or n>20:
    print("Error, valor mal ingresado")
    n=int(input("Numero de salidas: "))
v=int(input("Valor a procesar: "))
while v<0 or v>=10:
    print("Error, valor mal ingresado")
    v=int(input("Valor a procesar: "))
b=-1
c=1
p=1
x=1
g=0
print(v)

while x<=n:
    a=(v%10)
    if a==b:
        c=c+1
    else:
        g=g+c*(10**p)+a*(10**(p-1))
        b=a
        p=p+2
        c=1
    v=v//10
    if v==0:
        print(g)
        v=g
        g=0
        p=1
        x=x+1
        b=-1