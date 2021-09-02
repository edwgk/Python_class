import pandas as pd
def hallarAsociados(nombres:list,departamentos:list,nombreArchivo:str)->str:
    
    if nombreArchivo.endswith('datos_p79.csv'):
        e=1
    #    try:
    #        df=pd.read_csv(nombreArchivo, sep=';')
           
    #     except:

    #         return 'Error al leer el archivo de datos'
        
        
        
    else:
        return f'Error leyendo el archivo.'

    return

'''
def listaPeliculas(rutaFileCsv: str)-> str:
    if rutaFileCsv.split('.')[-1] != 'csv': 
        try:
            csv = pd.read_csv(rutaFileCsv)
            #print(csv)

            #Se selecciona la columna 'Year' como indice y la columna 'Gross Earnings' para aplicar la fórmula de resumen
            subGrupoPeliculas = csv[['Year', 'Gross Earnings']]
            #print(subGrupoPeliculas)
            #Con pivot_table indexamos 'Year'
            gananciaAno = subGrupoPeliculas.pivot_table(index=['Year'])
            return gananciaAno.head(10)
            #Se importa la libreria matplotlib.pyplot
            #import matplotlib.pyplot as plt
            #gananciaAno.plot()
            #Se muestra la columna 'Net Earnings' [76 rows x 1 columns]
            #print('\n Ganancia por Año')
            #Se muestra el resultado con la grafica
            #plt.show()
        except:  
            print('Error al leer el archivo de datos.')
    else:
        return 'Extensión inválida.'
    

#ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022/blob/3f3847bbf2dbe4b2cf4dcceb96a455d92c88f9c5/movies.csv?raw=true' 
print(listaPeliculas(rutaFileCsv))
'''




nombres=['Rachel','grey']
departamentos=['Ventas','Ventas']

# nombres=['rachel','mary','karj','nasaam']
# departamentos=['Oficina','Oficina','Oficina','Oficina']

# nombres=['jean']
# departamentos=['']

# nombres=['']
# departamentos=['']

# nombres=['jhin']
# departamentos=['ventas','Ingenieria']

print(hallarAsociados(nombres,departamentos,'https://raw.githubusercontent.com/anfejaramillo/OpenAccess/main/datos1_p79.csv'))

# https://raw.githubusercontent.com/anfejaramillo/OpenAccess/main/datos_p79.csv