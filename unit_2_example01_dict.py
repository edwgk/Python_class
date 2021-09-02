#18-5-21
def promedionotas2(dicnotas):
    sumatoria=0
    sumatoria+=dicnotas["nota1"]
    sumatoria+=dicnotas["nota2"]
    sumatoria+=dicnotas["nota3"]
    sumatoria+=dicnotas["nota4"]
    promedio=round(sumatoria/4,2)
    #round redondear a 2 decimales
    return promedio

dicnotas={}
dicnotas["nota1"]=3.0
dicnotas["nota2"]=2.1
dicnotas["nota3"]=5.0
dicnotas["nota4"]=4.7
print("el promedio es",promedionotas2(dicnotas))
