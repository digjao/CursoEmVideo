distance = int(input('Digite a distancia da viagem: '))
print('Você está prestes a começar uma viagem de {}km'.format(distance))
if distance <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(distance*0.5))
else:
    print('E o preço da sua viagem será de R${:.2f}'.format(distance*0.45))
