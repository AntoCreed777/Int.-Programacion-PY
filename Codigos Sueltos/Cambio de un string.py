txt=str(input("Ingrese su cadena de caracteres: "))
while len(txt)>1000:
    txt=str(input("Valor fuera de rango\nIngrese su cadena de caracteres: "))

txt=txt.replace("1","I")
txt=txt.replace("3","E")
txt=txt.replace("4","A")
txt=txt.replace("5","S")
txt=txt.replace("7","T")
txt=txt.replace("0","O")
txt=txt.replace("8","B")
print(txt)