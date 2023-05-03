k=int(input("Numero de consultas a ingresar: "))
while k<=0 or k>1000:
    print("Error, valor mal ingresado")
    k=int(input("Numero de consultas va a ingresar: "))

n=int(input("Coordenada X: "))
while n<=0 or n>1000:
    print("Error, valor mal ingresado")
    n=int(input("Coordenada X: "))

m=int(input("Coordenada Y: "))
while m<=0 or m>1000:
    print("Error, valor mal ingresado")
    m=int(input("Coordenada Y: "))

while k!=0:
    x=int(input("Coordenada X: "))
    while x<=0 or x>1000:
        print("Error, valor mal ingresado")
        x=int(input("Coordenada X: "))
    
    y=int(input("Coordenada Y: "))
    while y<=0 or y>1000:
        print("Error, valor mal ingresado")
        y=int(input("Coordenada Y: "))
    if x==n or y==m:
        print("Esta en la Frontera")
    if x>n:
        if y>m:
            print("Nlogonia Noroccidental")
        print("Nlogonia Sudoriental")
    if y>m:
        print("Nlogonia Nororiental")
    else :
        print("Nlogonia Sudoccidental")
    k=k-1
