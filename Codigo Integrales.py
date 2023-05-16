from numba import njit
import time
#@njit
def factorial(n):
    a=1
    m=n
    while n>0:
        a=a*n
        n=n-1
    return a
#@njit
def coseno(a,r):
    c=0
    for b in range(r):
         c+=(((-1)**b)*(a**(2*b)))/factorial(2*b)
    return(c)
#@njit
def seno(a,r):
    c=0
    for b in range(r):
         c+=(((-1)**b)*(a**(2*b+1)))/factorial(2*b+1)
    return(c)
##@njit
def integral(vi,vf,p):
    I=int(((vf**(p+1))-(vi**(p+1)))/(p+1))
    print(I)
#@njit
def integralseno(vi,vf,p):
    c=0
    i=0
    delta=vf-vi
    b=delta/p
    while i<=delta:
        c+=b*seno((vi+i),30)
        i=i+b
    print(c)
#@njit
def integralcoseno(vi,vf,p):
    c=0
    i=0
    delta=vf-vi
    b=delta/p
    while i<=delta:
        c+=b*coseno((vi+i),30)
        i=i+b
    print(c)

start=time.perf_counter()
integralcoseno(3,8,10000)
end=time.perf_counter()
print("IntegralCoseno(con numba) = {}s".format((end - start)))

"""
start = time.perf_counter()
integralcoseno(3,4,1000000)
end = time.perf_counter()
print("Elapsed on IntegralCoseno(without numba) = {}s".format((end - start)))


for i in range(10):
   start = time.perf_counter()
   integralseno(3,4,1000000)
   end = time.perf_counter()
   print("Elapsed on IntegralSeno(with numba) = {}s".format((end - start)))
"""

"""
q=str(input("¿Que tipo de Integral desea hacer, Normal o Trigonometrico?? "))
while q!="Normal"and q!="Trigonometrico":
    q=str(input("Valor mal ingresado, vuelva a intentarlo\n¿Que tipo de Integral desea hacer, Normal o Trigonometrico?? "))

if q=="Normal":
    integral(int(input("Valor Inicial: ")),int(input("Valor Final: ")),int(input("Potencia: ")))
if q=="Trigonometrico":
    q=str(input("¿De que formula, Seno o Coseno?? "))
    while q!="Seno"and q!="Coseno":
        q=str(input("Valor mal ingresado, vuelva a intentarlo\n¿De que formula, Seno o Coseno??  "))
    if q=="Seno":
        integralseno(float(input("Ingrese el valor inicial: ")),float(input("Ingrese el valor final: ")),float(input("Ingrese la presicion: ")))
    if q=="Coseno":
         integralcoseno(float(input("Ingrese el valor inicial: ")),float(input("Ingrese el valor final: ")),float(input("Ingrese la presicion: ")))
"""