import numpy as np

list=[]
for i in range(16):
    list.append(float(input(f"Ingrese su dato {i+1} numeros: ")))
vector=np.array(list)
mitad1=0
mitad2=0
for i in range(8):
    mitad1+=vector[i]
for i in range(8,16):
    mitad2+=vector[i]
print(mitad1)
print(mitad2)