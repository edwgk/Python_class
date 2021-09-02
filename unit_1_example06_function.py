def saludar(nombre,mensaje='msj por defecto'):
    #mspor defecto por si falta un parametro
    #msj por defecto van despues de argumentos que no tengan msj x defecto
    print(mensaje,nombre)
    return mensaje + '_' + nombre

cadenaCaracteres=saludar('Oscar','Mensaje prueba')
print(cadenaCaracteres)

cadenaCaracteres2=saludar('Oscar')
print(cadenaCaracteres2)
