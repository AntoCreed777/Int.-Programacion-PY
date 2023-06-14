def fibonachi(x):
    a=1
    b=1
    n=0
    while n<=1000:
        n=n+1
        c=b
        b=a+b
        a=c
        if x==a:
            return(n)
        if n==100:
            print("El valor no es un numero de fibonachi en el intervalo de 0 a 100")

N=int(input("Cuantos casos desea evaluar? "))
while N<=0 or N>5:
    N=int(input("Cuantos casos desea evaluar? "))

for i in range(N):
    P=int(input("Cuantas palabras? "))
    while P<=0:
        P=int(input("Cuantas palabras? "))
    for j in range():
        P=int(input("Cuantas palabras? "))
        while P<=0:
            P=int(input("Cuantas palabras? "))