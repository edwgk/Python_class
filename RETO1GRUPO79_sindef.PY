
n1=int(input('Primer Numero a comprobar '))
n2=int(input('Segundo Numero a comprobar '))
n3=int(input('Tercer Numero a comprobar '))
n4=int(input('Cuarto Numero a comprobar '))
n5=int(input('Quinto Numero a comprobar '))
#menor_de_cinco(562,889,761,356,1352)
#mayor_de_cinco(56,895,5942,1153,1592)
numeromenor=min(n1,n2,n3,n4)
numeroi=max(n1,n2,n3,n4)
if numeromenor<n5:
    print ('El numero menor de entre los introducidos es el: {',numeromenor,'} donde {',numeromenor,'} es el menor de los cinco numeros introducidos')
if numeroi>n5:
    print ('El numero {',numeroi,'} es mayor al {',n5,'}')
