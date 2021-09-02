fruta='fresa'
longitudcadena1=fruta.__len__()
longitudcadena2=len(fruta)
print(f'las longitudes son {longitudcadena1} y {longitudcadena2}')
letra=fruta[1]
print(letra)

cadena='OscarVel'
subcadena=cadena[0:3] #mostrar parte de la cadena empieza en 0 hasta posicion q se necesita+1
print(subcadena)
subcadena1=cadena[3:] #posicion3 hasta el ultimo
print(subcadena1)

saludo = '¡Hola, mundo!'
nuevo_saludo = 'J' + saludo[1:]
print(nuevo_saludo)

print('a' in 'banana')

palabra = 'piña'
# if palabra == 'banana':
#     print('Está bien, bananas')

if palabra < 'banana': #el > o < compara alfabeticamente strings
    print('Tu palabra, ' + palabra + ', viene antes de banana')
elif palabra > 'banana':
    print('Su palabra, ' + palabra + ', viene después de banana.')
else:
    print('Está bien, su palabra es banana')