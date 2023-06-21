import numpy as np
def preguntas(N):
    if N=="":
        return "nada"
    elif N.isdigit()==False:
        return "nonum"
    else:
        return True
def ingresonumero(mensaje):
    N=str(input(f"{mensaje}"))
    while True:
        aux=preguntas(N)
        if aux==True:
            N=int(N)
            return(N)
        if aux=="nada":
            N=str(input(f"\nPor favor, ingrese un dato\n{mensaje}"))
        if aux=="nonum":
            N=str(input(f"\nSolo se aceptan numeros\n{mensaje}"))
        if aux=="escero":
            N=str(input(f"\nEl 0 no es valido\n{mensaje}"))

filas=ingresonumero("Ingresa la cantidad de filas: ")
columnas=ingresonumero("Ingresa la cantidad de columnas: ")

while filas >100 or filas<5:
    filas=ingresonumero("\nError\nIngresa la cantidad de filas: ")
while columnas >100 or columnas<5:
    columnas=ingresonumero("\nError\nIngresa la cantidad de columnas: ")

matrizhueca=np.zeros((filas,columnas),dtype=int)
nuemrosingreso=[]
for i in range(filas):
    for j in range(columnas):
        numero=ingresonumero(f"Ingrese el numero en la fila {i+1} y en la columna {j+1}: ")
        if numero!=0:
            nuemrosingreso.append(numero)
        matrizhueca[i][j]=numero


matrizresultado=np.zeros((len(nuemrosingreso),3),dtype=int)

for i in range(len(nuemrosingreso)):
    posicionf=np.where(matrizhueca==nuemrosingreso[i])[0][0]
    posicionc=np.where(matrizhueca==nuemrosingreso[i])[1][0]
    matrizresultado[i][0]=posicionf
    matrizresultado[i][1]=posicionc
    matrizresultado[i][2]=nuemrosingreso[i]
print(matrizresultado)