def validacion(string,L):
    if len(string)!=L:
        return(False)
    else:
        return(True)
def palabraparecida(Q,palabras,similitud):
    for i in range(len(palabras)):
        if i ==0:
            palabraparecida=palabras[i]
            parecidomayor=similitud[i]
        palabra=palabras[i]
        parecido=similitud[i]
        if parecido>parecidomayor:
            parecidomayor=parecido
            palabraparecida=palabra
    return(palabraparecida)
Q=int(input("Ingrese la cantidad de palabras: "))
L=int(input("Ingrese la cantidad de letras: "))

palabramaster=str("Ingrese la palabra master: ")
if validacion(palabramaster)==False:
    palabramaster=str(f"\nDebe tener {L} letras\nIngrese la palabra master: ")
palabras=[]
for i in range(Q-1):
    palabra=str("Ingrese la palabra: ")
    if validacion(palabra)==False:
        palabra=str(f"\nDebe tener {L} letras\nIngrese la palabra: ")
        palabras.append(palabra)

similitud=[]
for i in range(Q-1):
    contador=0
    for j in range(L):
        if palabras[i][j]==palabramaster[j]:
            contador+=1
        if palabras[i][j]!=palabramaster[j] or j==L:
            similitud.append(contador)
            break

resultado=[]
resultado.append(palabramaster)

for i in range(Q):
    palabraparecida=palabraparecida(Q,palabras,similitud)
    resultado.append(palabraparecida)
    palabras.remove(palabraparecida)
print(resultado)