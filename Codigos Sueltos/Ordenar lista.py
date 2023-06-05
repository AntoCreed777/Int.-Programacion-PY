def menor(list):
    menor=list[0]
    cantidad=len(list)
    menor=int(menor)
    for i in range(cantidad):
        if menor>int(list[i]):
            menor=list[i]
            menor=int(menor)
    return(menor)
def mayor(list):
    cantidad=len(list)
    mayor=list[cantidad-1]
    mayor=int(mayor)
    for i in range(-1,-(cantidad+1),-1):
        if mayor<int(list[i]):
            mayor=list[i]
            mayor=int(mayor)
    return(mayor)
list=[]
c=int(input("Cuantos datos va a ingresar: "))
for i in range(c):
    x=str(input("Ingrese algun elemento: "))
    list.append(x)
print(list)
list.sort()
print(list)
print(f"El menor es {menor(list)} y el mayor es {mayor(list)}")