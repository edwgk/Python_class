#mensajes
'''mas mensajes'''
def promedio_salarial(Laura:int,Juan:int,Andres:int,Sara:int,Natalia:int)->str:
    promedio=round(((Laura*3600)+(Juan)+(Andres)+(Sara*3600)+(Natalia*3600))/5,2)
    return f'El promedio salarial es: {promedio} pesos colombianos'
pass
print(promedio_salarial(1050,1800000,2750000,2100,3500))

