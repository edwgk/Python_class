def reporte_ferreteria(productos_vendidos):
    
    total_precio=(productos_vendidos['producto1']["precio"])+(productos_vendidos['producto2']["precio"])+(productos_vendidos['producto3']["precio"])
    total_impuestos=((productos_vendidos['producto1']["precio"])*(productos_vendidos['producto1']["iva"]))+((productos_vendidos['producto2']["precio"])*(productos_vendidos['producto2']["iva"]))+((productos_vendidos['producto3']["precio"])*(productos_vendidos['producto3']["iva"]))
    mensaje="Los productos reportados son: "+(productos_vendidos['producto1']["nombre"])+" , "+(productos_vendidos['producto2']["nombre"])+" , "+(productos_vendidos['producto3']["nombre"])
    
    
    reporte={
        'precio_total':total_precio,
        'impuestos_total':total_impuestos,
        'reporte':mensaje
    }
    return reporte

print(reporte_ferreteria({'producto1' : {'nombre' : 'Varilla','precio' : 35250,'iva'    : 0.05,},'producto2' : {'nombre' : 'Cemento','precio'  : 60500,'iva'    : 0.15,},'producto3' : {'nombre' : 'Tubo PVC','precio'  : 10300,'iva'    : 0,}}))

# productos_vendidos={
#     'producto1':{
#         'nombre':'nombreproducto1',
#         'precio':precio,
#         'iva':porcentaje_iva
#     },
#     'producto2':{
#         'nombre':'nombreproducto2',
#         'precio':precio,
#         'iva':porcentaje_iva
#     },
#     'producto3':{
#         'nombe':'nombreproducto3',
#         'precio':precio,
#         'iva':porcentaje_iva
#      }
# }

# productos1={
#     'producto1':{
#         'nombre':'Varilla',
#         'precio':35250,
#         'iva':0.05
#     },
#     'producto2':{
#         'nombre':'Cemento',
#         'precio':60500,
#         'iva':0.15
#     },
#     'producto3':{
#         'nombre':'Tuvo PVC',
#         'precio':10300,
#         'iva':0
#      }
# }

# productos1={
#     'producto1':{
#         'nombre':'Llave',
#         'precio':1500,
#         'iva':0
#     },
#     'producto2':{
#         'nombre':'Cemento',
#         'precio':60500,
#         'iva':0.15
#     },
#     'producto3':{
#         'nombre':'Tornillos',
#         'precio':22500,
#         'iva':0.19
#      }
# }
# suma=0
# iva_suma=0
# rep=''
# suma=(productos1['producto1']["precio"])+(productos1['producto2']["precio"])+(productos1['producto3']["precio"])
# iva_suma=((productos1['producto1']["precio"])*(productos1['producto1']["iva"]))+((productos1['producto2']["precio"])*(productos1['producto2']["iva"]))+((productos1['producto3']["precio"])*(productos1['producto3']["iva"]))
# rep="Los productos reportados son: "+(productos1['producto1']["nombre"]) +", "+ (productos1['producto2']["nombre"]) + ", "+ (productos1['producto3']["nombre"])



# print(suma)
# print(iva_suma)
# print(rep)
# totalpagar1=reporte_ferreteria(productos1)

'''def generarreortesnotas(boletascalificaciones):
    sumatoria=0
    sumatoria=sumatoria+boletascalificaciones["nota1"]
    sumatoria=sumatoria+boletascalificaciones["nota2"]
    sumatoria=sumatoria+boletascalificaciones["nota3"]
    sumatoria+=boletascalificaciones["nota4"]
    prom=sumatoria/4
    reportenotas={
        "estudiante":boletascalificaciones["estudiante"],
        "promedio":prom


    }
    return reportenotas

def reportarpromedio (repnotas):
    return "el estudiante "+ repnotas ["estudiante"] + " tuvo un promedio de " + str(repnotas["promedio"])

calificaciones={
    "estudiante":"jose david",
    "nota1":3.0,
    "nota2":2.1,
    "nota3":5.0,
    "nota4":4.7
}
reportegenerado=generarreortesnotas(calificaciones)
reportepromedio=reportarpromedio(reportegenerado)
print(reportepromedio)
'''