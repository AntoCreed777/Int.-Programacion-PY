import numpy as np

list=[]
for i in range(12):
    list.append(int(input("Ingrese sus 12 numeros: ")))
vector=np.array(list)
print(vector)