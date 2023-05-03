n=int(input("Numero a evaluar: "))
while n<=0:
    print("Error, valor mal ingresado")
    n=int(input("Numero a evaluar:  "))
d=0
i=0
while n!=0:
    if n%2!=0:
        d=d+10**i
    n=n//2
    i=i+1
print(d)
