num = soma = cont = 0
num = int(input('Digte um número [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digte um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))



