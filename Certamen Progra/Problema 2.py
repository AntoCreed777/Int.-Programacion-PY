def validaentrada(x):
    global romanos
    for i in range(len(x)):
        if x[i] not in romanos:
            return False
    return True
def validaromano(x):
    global romanos
    for i in range(len(x)):
        aux=romanos.index(x[i])
        for j in range(i+1,len(x)):
            aux2=romanos.index(x[j])
            if aux<aux2:
                return False
    return True
def validacantidar(x):
    letrasrepetibles=["M","C","X","I"]
    for i in range(len(x)):
        if x[i] in letrasrepetibles:
            aux=x[i]
            if x.count(aux)>3:
                return False
def validacantidan(x):
    letrassolitarias=["D","L","V"]
    for i in range(len(x)):
        if x[i] in letrassolitarias:
            aux=x[i]
            if x.count(aux)>1:
                return False
def resta(x):
    global valor
    for i in range(x):
        if x[i]=="I":
            if i+1>len(x):
                None
            elif x[i+1]=="V" or x[i+1]=="X":
                valor=valor-2
        if x[i]=="X":
            if i+1>len(x):
                None
            elif x[i+1]=="L" or x[i+1]=="C":
                valor=valor-20
        if x[i]=="C":
            if i+1>len(x):
                None
            elif x[i+1]=="D" or x[i+1]=="M":
                valor=valor-200

romanos=["I","V","X","L","C","D","M"]
VALORROMANOS=[1,5,10,50,100,500,1000]

Numero=str(input("Ingrese su numero romano: "))

while True:
    if validaentrada(Numero)==False:
        Numero=str(input("\nSolo se aceptan romanos\nIngrese su numero romano: "))
    elif validaromano(Numero)==False:
        Numero=str(input("\nVerifique que esta bien escrito su numero\nIngrese su numero romano: "))
    elif validacantidar(Numero)==False:
        Numero=str(input("\nError, revise su nuemro\nIngrese su numero romano: "))
    elif validacantidan(Numero)==False:
        Numero=str(input("\nError, revise su nuemro\nIngrese su numero romano: "))
    else:
        break

valor=0

for i in range(len(Numero)):
    posicion=romanos.index(Numero[i])
    v=VALORROMANOS[posicion]
    valor=valor+v
resta()
print(valor)