def reporteCreditoSupermercado(calificaciones:list,nombres:dict)->str:
    
    print(len(calificaciones))
    print(len(nombres))
    if len(calificaciones)!=len(nombres):
        mensaje='Error generando el reporte: Los parámetros deben tener el mismo numero de elementos'


    reporteCreditos={
        'reporte':'{reporteCreditos}',
        'mensaje':'{resumen}'
    }
    
    return mensaje



# calificaciones=[
#     (numeroIdentificacionPesona1,'{CalificacionPersona1}'),
#     (numeroIdentificacionPesona2,'{CalificacionPersona2}'),
#     (numeroIdentificacionPesona3,'{CalificacionPersona3}'),
# ]
# nombres={
#     numeroIdentificacionPesona1:'nombePersona1',
#     numeroIdentificacionPesona2:'nombePersona2',
#     numeroIdentificacionPesona3:'nombePersona3',
# }

# calificaciones=[
#     (13104340,'{Aprobado}'),
#     (87432212,'{Desaproba}'),
#     (12830802,'{Desaprobado}')
# ]
# nombres={
#     87432212:'Mario',
#     13104340:'Juan',
#     12830802:'Marina'
# }

calificaciones=[
    (27519229,'{Aprobado}'),
    (73144493,'{Desaproba}'),
    (48627755,'{Desaprobado}')
]
nombres={
    11636305:'Miguel',
    73144493:'Milena',
    48627755:'Gener',
    27519229:'Luis'
}

print(reporteCreditoSupermercado(calificaciones,nombres))


# reporte de creditos sera una cadena de texto vacia si:
#       el número de elementos de la lista de calificaciones y el número de elementos del diccionario de nombres son diferentes o si alguno de los parámetros no tiene elementos
#       El valor de {resumen} será “Error generando el reporte: Los parámetros deben tener el mismo numero de elementos
#   Si el número de elementos de la lista de calificaciones es diferente al número de elementos del diccionario de nombres
#       {resumen} tendrá el valor de “Error generando el reporte: El numero de elementos de los parametros debe ser mayor que cero.” 
#       Si alguno de los parámetros no tiene elementos.