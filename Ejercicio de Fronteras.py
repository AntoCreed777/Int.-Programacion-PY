k=int(input("Numero de consultas a ingresar: "))
while k<=0 or k>1000:
    print("Error, valor mal ingresado")
    k=int(input("Numero de consultas va a ingresar: "))

n=int(input("Coordenada X: "))
while n<-1000 or n>1000:
    print("Error, valor mal ingresado")
    n=int(input("Coordenada X: "))

m=int(input("Coordenada Y: "))
while m<-1000 or m>1000:
    print("Error, valor mal ingresado")
    m=int(input("Coordenada Y: "))

while k!=0:
    x=int(input("Coordenada X: "))
    while x<-1000 or x>1000:
        print("Error, valor mal ingresado")
        x=int(input("Coordenada X: "))
    
    y=int(input("Coordenada Y: "))
    while y<-1000 or y>1000:
        print("Error, valor mal ingresado")
        y=int(input("Coordenada Y: "))
    if x==n or y==m:
        print("Esta en la Frontera")
    else:
        if x>n:
            if y>m:
                print("Nlogonia Nororiental")
            else:
                print("Nlogonia Sudoriental")
        else:
            if y>m:
                print("Nlogonia Noroccidental")
            else :
                print("Nlogonia Sudoccidental")
    k=k-1
