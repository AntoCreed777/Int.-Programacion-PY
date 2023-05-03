a=input("Ingrese la coordenada X del primer hito: ")
b=input("Ingrese la coordenada Y del primer hito: ")
c=input("Ingrese la coordenada Z del primer hito: ")
i=input("Ingrese la coordenada X del segundo hito: ")
j=input("Ingrese la coordenada X del segundo hito: ")
k=input("Ingrese la coordenada X del segundo hito: ")

Distancia1=(((i-a)**2)+((j-b)**2)+((k-c)**2))**0.5

a=input("Ingrese la coordenada X del primer hito: ")
b=input("Ingrese la coordenada Y del primer hito: ")
c=input("Ingrese la coordenada Z del primer hito: ")
i=input("Ingrese la coordenada X del segundo hito: ")
j=input("Ingrese la coordenada X del segundo hito: ")
k=input("Ingrese la coordenada X del segundo hito: ")

Distancia2=(((i-a)**2)+((j-b)**2)+((k-c)**2))**0.5  


Magnitud=((Distancia1 - Distancia2)**2)**0.5

print(Distancia1)
print(Distancia2)
print(Magnitud)
