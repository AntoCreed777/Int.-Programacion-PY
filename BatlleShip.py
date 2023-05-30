def eliminarcaracter(s,p,digitos):
    lista=list(s)
    a=p
    for i in range(digitos):
        lista.pop(a)
        a=a-1
    lista=("").join(lista)
    return lista
def coordenadasverticales(coordenada):
        guardadomomentaneo={}
        coordenada=int(coordenada)
        coordenada=coordenada-1
        coordenada=str(coordenada)
        coordenada=coordenada.zfill(digitos*2)
        for q in range(3):
                guardadomomentaneo.setdefault((i+1),coordenada)
                coordenada=int(coordenada)
                coordenada=coordenada+1
                coordenada=str(coordenada)
                coordenada=coordenada.zfill(digitos*2)
        return(guardadomomentaneo)
def coordenadashorizontales(coordenada):
        guardadomomentaneo={}
        coordenada=int(coordenada)
        coordenada=coordenada-10**digitos
        coordenada=str(coordenada)
        coordenada=coordenada.zfill(digitos*2)
        for q in range(3):
                guardadomomentaneo.setdefault(coordenada,(i+1))
                coordenada=int(coordenada)
                coordenada=coordenada+10**digitos
                coordenada=str(coordenada)
                coordenada=coordenada.zfill(digitos*2)
        return(guardadomomentaneo)
def coordenadacentral():
    coordenada=int(input(f"Ingrese la Coordenada Central de su {i+1}°barco: "))
    coordenada=str(coordenada)
    coordenada=coordenada.zfill(digitos*2)
    if sinbarcosjugador.count(coordenada)==0:
        coordenada=int(input(f"----------\nCelda invalida\nIngrese de nuevo la Coordenada Central de su {i+1}°barco: "))
        coordenada=str(coordenada)
        coordenada=coordenada.zfill(digitos*2)
    return(coordenada)

N=int(input("Ingrese el tamaño del tablero: "))
while N<10 or N>1000:
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
    coordenada=coordenadacentral()
    orientacion=str(input(f"Ingrese la horientacion de su {i+1}!Barco(V o H): "))
    while orientacion !="V" and orientacion !="H":
        orientacion=str(input(f"----------\nValor erroneo, vuelva a ingresarlo\nIngrese la horientacion de su {i+1}°Barco(V o H): "))
    if orientacion == "V":
        while sinbarcosjugador.count(coordenadasverticales(coordenada))==0:
             coordenada=coordenadacentral
        barcosjugador.setdefault(coordenadasverticales,(i+1))
    if orientacion == "H":
        while sinbarcosjugador.count(coordenadashorizontales(coordenada))==0:
             coordenada=coordenadacentral
        barcosjugador.setdefault(coordenadashorizontales,(i+1))
 
        #FALTA RESTRINGIR LA SELECCION DE CELDAS DEPENDIENDO DEL LUGAR
print(barcosjugador)
print(sinbarcosjugador)