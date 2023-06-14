import numpy as np

list=[]
for i in range(16):
    list.append(int(input(f"Ingrese su dato {i+1} numeros: ")))
vector=np.array(list)
print(min(vector))
print(max(vector))