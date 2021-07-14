compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?: '))
if opção == 1:
    print('O valor para pagamento à vista, com 10% de desconto sai a R${}'.format(compras - (compras*0.1)))
elif opção == 2:
    print('O valor para pagamento a vista no cartão sai a R${}'.format(compras-(compras*0.05)))
elif opção == 3:
    print('Em 2x no cartão, o valor da parcela ficaria R${}, sem juros!'.format(compras/2))
elif opção == 4:
    print('Parcelando em 3x no cartão, com 20% de juros, o valor da parcela ficaria em R$ {}'.format((compras*1.2)/3))
