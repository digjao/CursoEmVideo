casa = int(input('Qual o valor da casa?: R$'))
salario = float(input('Qual o seu salário mensal?: R$'))
anos =  int(input('Em quantos anos você pretende pagar a casa?: '))
prestação = casa / (anos * 12)
minimo = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser concedido! ')
else:
    print('Emprestimo NEGADO!')