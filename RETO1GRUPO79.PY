def menor_de_cinco(numero1:int,numero2:int,numero3:int,numero4:int,numero5:int)->str:
    numeromenor=min(numero1,numero2,numero3,numero4)
    numeroi=max(numero1,numero2,numero3,numero4)
    if (numeroi>numero5):
        return f'El numero {numeroi} es mayor al {numero5}'
    if (numeromenor<numero5):
        return f'El numero menor de entre los introducidos es el: {numeromenor}'
pass

n1=int(input('Primer Numero a comprobar '))
n2=int(input('Segundo Numero a comprobar '))
n3=int(input('Tercer Numero a comprobar '))
n4=int(input('Cuarto Numero a comprobar '))
n5=int(input('Quinto Numero a comprobar '))
#menor_de_cinco(562,889,761,356,1352)
#mayor_de_cinco(56,895,5942,1153,1592)
#numeromenor=min(n1,n2,n3,n4)
#

print (menor_de_cinco(n1,n2,n3,n4,n5))



