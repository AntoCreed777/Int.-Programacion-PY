import numpy as np
import random
N=int(input("Tamaño del array: "))
while N>10 or N<=0:
    N=int(input("Tamaño del array: "))  
vector=np.empty((N,N))
for i in range(N):
    for j in range(N):
        #vector[i][j]=int(input(f"Ingrese el numero en la fila {i+1} y en la columna {j+1}: "))
        vector[i][j]=random.randint(1,100)
        #vector[i][j]=i+j
print(vector)
for i in range(N):
    mayor=max(vector[:,i])
    posicionf=np.where(vector==mayor)[0][0]
    for j in range(N):
        posicionant=posicionf-(j+1)
        if posicionant==-1:
            vector[i,i]=mayor
        elif posicionant>0:
            vector[posicionf-j,i]=vector[posicionant,i]
for i in range(N):
    for j in range(N):
        j=i+1
        vector[i,j:]=0
    
print(f"\n{vector}")