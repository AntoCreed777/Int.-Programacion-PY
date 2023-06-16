import numpy as np
import random
def simetria(vector):
    for i in range(N):
        for j in range(i+1,N):
            if vector[i][j]!=vector[j][i]:
                return("No es simetrica")
    return("Es simetrica")

N=int(input("Tamaño del array: "))
while N>10 or N<=0:
    N=int(input("Tamaño del array: "))  
vector=np.empty((N,N))
for i in range(N):
    for j in range(N):
        vector[i][j]=int(input(f"Ingrese el numero en la fila {i+1} y en la columna {j+1}: "))
        #vector[i][j]=random.randint(1,100)
        #vector[i][j]=i+j
print(vector)
print(simetria(vector))