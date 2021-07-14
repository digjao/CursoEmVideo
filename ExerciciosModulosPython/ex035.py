salario = int(input('Qual o valor do seu salario hoje?: R$'))
if salario > 1250:
    print('Quem ganhava R${} passa a ganhar R${:.2f}'.format(salario, (salario*1.1)))
else:
    print('Quem ganhava R${} passa a ganhar R${:.2f}'.format(salario, (salario*1.15)))
