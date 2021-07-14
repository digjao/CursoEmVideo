velo = int(input('A velocidade do carro é: '))
if velo > 80:
    print('Você foi multado, pois a velocidade permitida é até 80Km/h')
    print('O valor da sua multa será de: R${:.2f} '.format((velo-80)*7))
print('Tenha um bom dia, dirija com segurança!')

