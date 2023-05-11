n=int(input("Numero de salidas: "))
while n<=0 or n>20:
    print("Error, valor mal ingresado")
    n=int(input("Numero de salidas: "))
v=int(input("Valor a procesar: "))
while v<0 or v>=10:
    print("Error, valor mal ingresado")
    v=int(input("Valor a procesar: "))
m=n
g=0
i=0
c=0
b=-1
while n>0:
    a=(v%10)
    if a==b:
        d=d+1
    else:
       if b!=-1:
            g=g+d*(10**(i-1))+b*(10**(i-2))
       else:
           print(a)
       d=1
       b=a
       i=i+2
    if v==0:
        v=g
    v=v//10
    n=n-1
    if n!=(m-1):
        print(g)