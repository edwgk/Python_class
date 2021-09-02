#12-05-21
def parqueadero_buses (cantidad_bus,ultimodigitonumero_bus):
    #los parqueaderops si estan llenos los mandamos al parq siguiente
    ocupacion_parqueadero1=5
    ocupacion_parqueadero2=10
    ocupacion_parqueadero3=7
    cambiarparqueadero=False
    if ultimodigitonumero_bus==1:
        if ocupacion_parqueadero1<cantidad_bus:
            return 1
        else:
            cambiarparqueadero=True

    if ultimodigitonumero_bus==2:
        if ocupacion_parqueadero2<cantidad_bus:
            return 2
        else:
            cambiarparqueadero=True
    if ultimodigitonumero_bus==3:
        if ocupacion_parqueadero1<cantidad_bus:
            return 3
        else:
            cambiarparqueadero=True
    if ultimodigitonumero_bus==1 or cambiarparqueadero:
        if ocupacion_parqueadero1<cantidad_bus:
            return 1

tamanoparqueadero=10
ultimodigito=2
parqueaderoparaelbus=parqueadero_buses(tamanoparqueadero,ultimodigito)
print(f'el parqueadero asignado para el bus es es:{parqueaderoparaelbus}')
