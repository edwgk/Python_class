# def constructorDeAcronimos(texto:str)->str:
#     texto = ''.join(texto[0] for texto in texto.upper().split()) 
#     return





# print('escriba algo:')
# texto1=str(input())
# constructorDeAcronimos(texto1)




# words = "There ain't no such thing as a free lunch." 
# acronym = ''.join(word[0] for word in words.upper().split()) 
# print (acronym)

def constructorDeAcronimos(cadena): 
    texto=""
    ev=0
    if cadena==" ":
        texto="El texto introducido esta vacío y por tanto no hay acronimo"
    elif cadena!="":
        letra1 = cadena[0]
        ev+=1
        texto=texto + "La primera letra de la palabra "+str(ev)+ " es "+ cadena[0] +". " 
        for i in range(1, len(cadena)): 
            
            if cadena[i-1] == ' ':
                ev=ev+1 
                texto=texto + "La primera letra de la palabra "+str(ev)+ " es "+ cadena[i] +". "
                letra1 += cadena[i]
                
        letra1 = letra1.upper()
        texto=texto + "El acronimo del texto introducido es: "+letra1
    return texto

texto = ""
print(constructorDeAcronimos(texto)) 
# inpt1 = "National Aeronautics Space Administration"
#inpt1="Campo Electro Magnetico"
# print(fxn(inpt1)) 