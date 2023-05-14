def factorial(n):
    a=1
    while n>0:
        a=a*n
        n=n-1
    return a
def coseno(a,r):
    c=0
    for b in range(r):
         c+=(((-1)**b)*(a**(2*b)))/factorial(2*b)
    return(c)
def seno(a,r):
    c=0
    for b in range(r):
         c+=(((-1)**b)*(a**(2*b+1)))/factorial(2*b+1)
    return(c)
def integral(vi,vf,p):
    I=int(((vf**(p+1))-(vi**(p+1)))/(p+1))
    print(I)
def integraltri(vi,vf,p):
    c=0
    i=0
    delta=vf-vi
    b=delta/p
    while i<=delta:
        c+=b*seno((b+i),50)
        i=i+b
    print(c)
integraltri(0,10,int(input("Presicion: ")))

q=str(input("¿Que tipo de Integral desea hacer, Normal o Trigonometrico?? "))
while q!="Normal"and q!="Trigonometrico":
    q=str(input("Valor mal ingresado, vuelva a intentarlo\n¿Que tipo de Integral desea hacer, Normal o Trigonometrico?? "))

if q=="Normal":
    integral(int(input("Valor Inicial: ")),int(input("Valor Final: ")),int(input("Potencia: ")))
#if q=="Trigonometrico":
    