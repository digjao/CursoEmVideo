r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo ', end='')
    if r1 == r2 and r2 == r3:
        print('equlátero!')
    elif r1 != r2 and r2 != r3 and r1!= r3:
        print('escaleno')
    else:
        print('isóceles')
