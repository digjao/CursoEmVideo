n1 = float(input('Digite a quantia em real é R$:'))
dollar = n1/5.22
euro = n1/6.35
libra = n1/7.39
print('O valor em dollar é: U${:.2f}, o valor em euros é: EUR{:.2f}, o valor em libras esterlinas é: ${:.2f}'.format(dollar, euro, libra))