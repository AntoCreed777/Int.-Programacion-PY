var="Hola Mundo soy antonio"
varconsalto="Hola Mundo\nsoy antonio"
autos=["Chevrolet","Suzuki","Toyota"]
#print(var) #impime todo el contenido de la variable

#print(len(var))    #imprime la cantidad de caracteres de la variable

#print(var[5])  #imprime el caracter en la posicion x+1 de la variable

#print(var[-10])    #imprime el caracter en la posicion desde la ultima letra, la posicion 0 es igual a la -10 en este caso

#print(var.split(" "))  #split separa el string segun lo que se le indique en los parentecis

#print(var.rsplit(" "))  #split separa el string segun lo que se le indique en los parentecis

#print(varconsalto.splitlines())  #split separa el string en los saltos de linea,en () se indica si se incluye el salto o no (True) o (False)

#print(var.strip())  #elimina caracteres, de froma predeterminada los espacios, o lo que se le especifique, solo del inicio o del final

#print(var.index("o")) #entrega el valor de la primera posicion que se encuentra lo que se busca, el de la primera letra

#print(var.rindex("o")) #entrega el valor de la ultima posicion que se encuentra lo que se busca, el de la primera letra

#print(var.count("o"))   #cuenta la cantidad de vece que se repite la cadena de caracteres

#print(",".join(autos))  #une los strings en una sola linea, se debe especificar el conector

#print(var.find("o"))    #encuentra al primer lugar en que encuentra lo que busca

#print(var.rfind("o"))    #encuentra al ultimo lugar en que encuentra lo que busca

#print(var.replace("o","a")) #reeemplaza el primer caracter que se ingresa por el segundo, en este caso, todas las "o" por "a"

#print(var.swapcase())   #intercambia mayusculas por minusculas y viceversa, no se coloca nada en ()

#print(var.upper())  #comvierte todos los caracteres en mayusculas

#print(var.zfill(2)) #El método zfill() agrega ceros (0) al comienzo de la cadena, hasta que alcanza la longitud especificada.
                     #Si el valor del parámetro len es menor que la longitud de la cadena, no se realiza ningún relleno.