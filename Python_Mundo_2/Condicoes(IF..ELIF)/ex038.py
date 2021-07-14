num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
if num1 == num2:
    print('Não existe valor maior, os dois valores são iguais')
elif num1 > num2:
    print('O primeiro valor é maior')
else:
    print('O segundo valor é maior')