a=float(input("Ingrese la coordenada X del primer hito: "))
b=float(input("Ingrese la coordenada Y del primer hito: "))
c=float(input("Ingrese la coordenada Z del primer hito: "))
i=float(input("Ingrese la coordenada X del segundo hito: "))
j=float(input("Ingrese la coordenada Y del segundo hito: "))
k=float(input("Ingrese la coordenada Z del segundo hito: "))

Distancia1=(((i-a)**2)+((j-b)**2)+((k-c)**2))**0.5

a=float(input("Ingrese la coordenada X del primer hito: "))
b=float(input("Ingrese la coordenada Y del primer hito: "))
c=float(input("Ingrese la coordenada Z del primer hito: "))
i=float(input("Ingrese la coordenada X del segundo hito: "))
j=float(input("Ingrese la coordenada Y del segundo hito: "))
k=float(input("Ingrese la coordenada Z del segundo hito: "))

Distancia2=(((i-a)**2)+((j-b)**2)+((k-c)**2))**0.5  


Magnitud=((Distancia1 - Distancia2)**2)**0.5

Distancia1=str(Distancia1)
Distancia2=str(Distancia2)
Magnitud=str(Magnitud)


print("La distancia entre el primer hito y el segundo en el primer momento es de "+Distancia1)
print("La distancia entre el primer hito y el segundo en el segundo momento es de "+Distancia2)
print("El desplazamiento total es de "+Magnitud)
