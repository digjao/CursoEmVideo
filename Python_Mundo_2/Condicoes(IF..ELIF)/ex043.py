peso = float(input('Qual é o seu peso: (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
IMC = (peso/altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso')
elif IMC <= 25:
    print('Você está no peso ideal')
elif IMC <= 30:
    print('Você está com Sobrepeso')
elif IMC <=40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MORBIDA')