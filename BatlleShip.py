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
jugador=[]
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
        jugador.insert(1,coordenada)
        c=eliminarcaracter(coordenada,p,digitos)
        coordenada=[]
        coordenada.insert(1,c)
        y=int(y)
    coordenada=[]
    x=int(x)
computadora=jugador

barcostotales=int(input("Ingrese la cantidad de barcos en juego por jugador: "))
while barcostotales<=2 or barcostotales>N:
    barcostotales=int(input(f"----------\nValor fuera de rango\nDebe ser mayor a 2 y menor o igual a {N}\nIngrese la cantidad de barcos en juego por jugador: "))

barcosjugador={}
sinbarcosjugador=jugador
for i in range(barcostotales):
    for j in range(3):
        coordenada=int(input(f"Ingrese la {j+1}°Coordenada de su barco: "))
        coordenada=str(coordenada)
        coordenada=coordenada.zfill(digitos*2)
        if sinbarcosjugador.count(coordenada)==0:
            coordenada=int(input(f"Celda invalida\nIngrese de nuevo la {j+1}°Coordenada de su barco: "))
            coordenada=str(coordenada)
            coordenada=coordenada.zfill(digitos*2)
        barcosjugador.setdefault((i+1),coordenada)
        sinbarcosjugador.remove(coordenada)
print(barcosjugador)
print(sinbarcosjugador)