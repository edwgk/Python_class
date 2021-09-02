#13-5-21
temperaturafarenheittexto=input('Ingrese la temperatura en grados fahrenheit: ')
try:
    temperaturafarenheit=float(temperaturafarenheittexto)
    gradoscelcius=(temperaturafarenheit-32.0)*5.0/9.0
    print(gradoscelcius)
except ValueError as errorVE:
    print('Error de conversion del numero introducido')
except ZeroDivisionError as errorZD:
    print('Error, en el algoritmo de conversion')
except:
    print('Error')