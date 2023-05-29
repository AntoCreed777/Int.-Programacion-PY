def eliminarcaracter(s,p,digitos):
    lista=list(s)
    a=p
    for i in range(digitos):
        lista.pop(a)
        a=a-1
    lista=("").join(lista)
    return lista

N=int(input("Ingrese el tamaño del tablero: "))
while N<10:
    N=int(input("----------\nValor fuera de rango, debe ser mayor o igual a 10\nIngrese el tamaño del tablero: "))

x=N
digitos=0
while x!=0:
    x=x//10
    digitos=digitos+1

p=digitos*2-1
restantes=[]
coordenada=[]
for i in range(N):
    x=i+1
    x=str(x)
    x=x.zfill(digitos)
    coordenada.insert(1,x)
    for j in range(N):
        y=j+1
        y=str(y)
        y=y.zfill(digitos)
        coordenada.insert(2,y)
        coordenada=("").join(coordenada)
        restantes.insert(1,coordenada)
        c=eliminarcaracter(coordenada,p,digitos)
        coordenada=[]
        coordenada.insert(1,c)
        y=int(y)
    coordenada=[]
    x=int(x)
print(restantes)
