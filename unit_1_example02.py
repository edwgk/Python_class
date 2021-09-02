print('Comparar ultimo digito de 2 numeros enteros positivos')
print('Digite primer numero entero')
num1=int(input())
print('Digite segundo numero entero')
num2=int(input())
if num1<0:
    num1=num1*-1
if num2<0:
    num2=num2*-1
ud1=num1-int(num1/10)*10
ud2=num2-int(num2/10)*10

if ud1==ud2:
    print('El Ultimo digito es igual')
else:
    print('El Ultimo digito no es igual')
