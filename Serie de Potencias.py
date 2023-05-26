def multiplicacion(x,e):
    aux=0
    for i in range(e):
        aux=aux+x
    return(aux)
def potencia(x,e):
    aux=1
    for i in range(e):
        aux=multiplicacion(aux,x)
    return(aux)
a=-1
while a<0:
    x=int(input("Introdusca el numero a elevar: "))
    while x<0 or x>100:
        print("Valor fuera de rango")
        x=int(input("Introdusca el numero a elevar: "))
    e=int(input("Introdusca la potencia: "))
    while e<0 or e>1000:
        print("Valor fuera de rango")
        e=int(input("Introdusca la potencia: "))
    if x==0 and e==0:
        break
    print(f"{x} elevado a {e} es igual a {potencia(x,e)}")