N=str(input("Ingrese un valor: "))
d=("1","2","3","4","5","6","7","8","9")
for i in range(len(N)):
    if N[i] in d:
        None
    else:
        N=str(input("Solo se aceptan numeros\nIngrese un valor: "))
        i=0
print(N)