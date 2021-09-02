frase="Nat Ae Spe Adm"
n = len(frase)
frase = frase.upper()
i = 0
z = frase[i]

i = 1
z2="La primera letra de la palabra "+str(i)+" es " +z+" . "
while not(i>=(n-1)):
    if (frase[i]==' ' and  not(frase[i+1]=='D')):
        if not(frase[i+1]=='Y'):
            
             
            z = z + frase[i+1]
            z2+="La primera letra de la palabra "+str(i)+" es " +z+". "
            
    i = i + 1

print(z)
print(z2)