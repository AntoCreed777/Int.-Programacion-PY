import numpy as np

list=[]
for i in range(16):
    #list.append(int(input(f"Ingrese su dato {i+1} numeros: ")))
    list.append(i+1)
vector=np.array(list)
mayor=max(vector)
posicion=np.where(vector==mayor)[0][0]
print(posicion)