def fibonachi(list):
    x=maximo(list)
    a=1
    b=1
    numerofibo=[]
    while True:
        c=b
        b=a+b
        a=c
        a=str(a)
        numerofibo.append(a)
        a=int(a)
        if x==a:
            return(numerofibo)
def ingresodatos():
    cifrado=[]
    letras=[]
    PT=int(input("Cuantas letras? "))
    while PT<=0:
        PT=int(input("\n\nDebe ser mayor a 0\nCuantas letras? "))
    auxn=str(input("Ingrese el cifrado: "))
    cifrado=auxn.split()
    while len(cifrado)!=PT:
        auxn=str(input(f"\nDebe ingrear {PT} datos\nIngrese el cifrado: "))
        cifrado=auxn.split()
    auxp=str(input("Ingrese las letras cifradas: "))
    for i in range(len(auxp)):
        if auxp[i].isalpha()==True:
            letras.append(auxp[i])
    while len(letras)!=PT:
        auxp=str(input(f"\nDebe ingrear {PT} datos\nIngrese las letras cifradas: "))
        for i in range(len(auxp)):
            if auxp[i].isalpha()==True:
                letras.append(auxp[i])
    return(cifrado,letras,PT)
def maximo(list):
    b=0
    for i in range(len(list)):
        a=list[i]
        a=int(a)
        if a>b:
            b=a
    return(b)

N=int(input("Cuantos casos desea evaluar? "))
while N<=0 or N>5:
    N=int(input("\n\nSolo se aceptan numeros\nCuantos casos desea evaluar? "))

for i in range(N):
    cifrado,letras,PT=ingresodatos()
    numerofibo=fibonachi(cifrado)
    aux=[""]
    resultado=[]
    for i in range(len(numerofibo)):
        resultado.append(aux)
    for i in range(len(cifrado)):
        posicion=numerofibo.index(cifrado[i])
        resultado[posicion]=letras[i]


    print(resultado)