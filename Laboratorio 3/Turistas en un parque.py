T=0
J=0
while T>-1:
    a=str(input("¿ENTRADA o SALIDA? "))
    while a!="ENTRADA"and a!="SALIDA"and a!="FIN":
        a=str(input("¿Entrada o Salida? "))
    if a=="ENTRADA":
        t=int(input("Cantidad de turistas: "))
        while t<0 or t>20:
            print("Error, valor mal ingresado")
            t=int(input("Cantidad de turistas: "))
        T=T+t
        J=J+1
    if a=="SALIDA":
        if J-1>=0:
            t=int(input("Cantidad de turistas: "))
            while t<0 or t>20:
                print("Error, valor mal ingresado")
                t=int(input("Cantidad de turistas: "))
            while t>T:
                print("ERROR LOGICO")
                t=int(input("Cantidad de turistas: "))
                while t<0 or t>20:
                    print("Error, valor mal ingresado")
                    t=int(input("Cantidad de turistas: "))
            T=T-t
            J=J-1
        else:
            print("Error Logico")
    if a=="FIN":
        break

T=str(T)
J=str(J)
print("Hay "+T+" turistas en "+J+" jeeps dentro del parque.")