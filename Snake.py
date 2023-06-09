import os
def ingresonumero(mensaje):
    N=str(input(f"{mensaje}"))
    while True:
        while N=="":
            N=str(input(f"Por favor, ingrese un dato\n{mensaje}"))
        if N[0]=="-":
            N=str(input(f"Solo se aceptan numeros positivos\n{mensaje}"))
        if N.isdigit()==False:
            N=str(input(f"Solo se aceptan numeros\n{mensaje}"))
            i=0
        else:
            break
    return(N)
N=ingresonumero("Ingrese el tamaño del tablero: ")
N=int(N)
while N<10 or N>1000:
    N=ingresonumero("----------\nValor fuera de rango, debe ser mayor o igual a 10\nIngrese el tamaño del tablero: ")
    N=int(N)
print(N)
##############################################################
x=[]
matriz=[]
for i in range(N):
    x.append(" ")
for i in range(N):
    matriz.append(x)
##############################################################
while True:
    for i in range(len(matriz)):
        print(f"{matriz[i]}\n")
    os.system("cls")