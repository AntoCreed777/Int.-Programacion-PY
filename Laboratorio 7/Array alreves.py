import numpy as np

list=[]
for i in range(12):
    list.append(float(input("Ingrese sus 12 numeros: ")))
C=[]
for i in range(-1,-13,-1):
    C.append(list[i])
vector=np.array(C)
print(C)