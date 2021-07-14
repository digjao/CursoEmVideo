n = float(input('Digite a quantidade de Km percorridos pelo carro: '))
n1 = int(input('Digite a quantidade de dias que o carro ficou alugado: '))
km = n*0.15
di = n1*60
print('O valor total do aluguel do carro será de: R${},'.format(km+di))
