import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/anfejaramillo/OpenAccess/main/datos_p79.csv')
i=1
for i in df.index :
    n1=df.columns['nombre_1']
    n2=df.columns['nombre_1']
    if n1=='Rachel' or n2=='rachel':
        print(df['nombre_1'] + df['nombre_2'])


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