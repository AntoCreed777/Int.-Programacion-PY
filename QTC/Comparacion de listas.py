a=[]
p=["Antonio", "Manuel"]
b=int(input("Cuantos datos decea ingresar?  "))
while b<=0:
    b=int(input("Error, valor fuera de rango\nCuantos datos decea ingresar?  "))
for i in range(b):
    a.append(str(input()))

a.sort()
p.sort()

def Comparacion_listas(l1, l2):
    for x, y in zip(l1, l2):
        if x != y:
            return False
    return len(l1) == len(l2)

print(Comparacion_listas(a,p))