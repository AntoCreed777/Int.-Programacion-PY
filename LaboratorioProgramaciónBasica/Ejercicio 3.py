a=int(input("Ingrese un Valor"))
while a<=0:
    print("Error, valor mal ingresado")
    a=int(input("Ingrese un Valor"))


b=0
s=0
while b<=a:
    s=s+b
    b=b+2
print(s)