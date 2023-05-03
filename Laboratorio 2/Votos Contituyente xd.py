v=int(input("Ingrese la cantidad de votos: "))
while v<=0:
    print("Error, valor mal ingresado")
    v=int(input("Ingrese la cantidad de votos: "))
for i in range(v):
    voto:input("Ingrese el valor del voto(EJ: F,C,X o _) ")
    while voto!="F"or"C"or"X"or"_":
        print("Caracteres no validos")
        voto:input("Ingrese el valor del voto(EJ: F,C,X o _) ")

    f=0
    c=0
    x=0
    n=0

    if voto=="F":
        f=f+1
    if voto=="C":
        c=c+1
    if voto=="X":
        x=x+1
    if voto=="_":
        n=n+1

f=str(f)
c=str(c)
x=str(x)
n=str(n)

print("Hay "+f+" votos a favor")
print("Hay "+c+" votos en contra")
print("Hay "+x+" votos en blanco")
print("Hay "+n+" votos nulos")

f=int(f)
c=int(c)
x=int(x)
n=int(n)

apro=f+x
total=f+c+x
resultado= apro/total
if resultado >= (2/3):
    print("Iniciativa Aprovada")
else:
    print("Iniciativa Rechazada")


