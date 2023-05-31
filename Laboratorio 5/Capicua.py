def Capicua(txt):
    l=len(txt)
    for i in range(l):
        if txt[i]!=txt[-(i+1)]:
            return False
    return True

N=int(input("Ingrese el numero a evaluar: "))
while N<=0:
    N=int(input("Valor fuera de rango\nIngrese de nuevo el numero a evaluar: "))
N=str(N)

s=Capicua(N)
if s==True:
    print(N+" es Capicua")
else:
    print(N+" no es Capicua")