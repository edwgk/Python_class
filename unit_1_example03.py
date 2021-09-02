print("Este programa sirve para comparar el ultimo digito de dos numero enteros")
print("Por favor introduzca el primer numero")
texto1 = input()
print("Por favor introduzca el segundo numero")
texto2 = input()
if texto1.isnumeric() and texto2.isnumeric() :
    num2 = int(    texto2   )
    num1 = int(    texto1   )
    if   num1   <  0   :
        num1 = num1 * -1
    if num2 < 0 :
        num2 = -num2
    ud1 = num1 - int(num1 / 10) * 10
    ud2 = num2 - num2 // 10 * 10

    if ud1 == ud2 :
        print("El ultimo digito es igual")
    else:
        print("El ultimno digito es diferente")
else:
    print ('Alguna de las dos variables introducidas no son numeros')