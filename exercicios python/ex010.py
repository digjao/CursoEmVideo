chamar_soma = 'soma'
chamar_subtracao = 'subtracao'
chamar_divisao = 'divisao'
chamar_multi = 'multi'

chamar_operador = input('O que você quer? [soma], [subtracao], [divisao], [multi]: ')

if chamar_operador == chamar_soma:
    n1_soma = int(input('Digite um numero: '))
    n2_soma = int(input('Digite outro numero: '))


    def soma(n1, n2):
        return n1 + n2


    print(soma(n1_soma, n2_soma))

elif chamar_operador == chamar_subtracao:
    n1_subtracao = int(input('Digite um numero: '))
    n2_subtracao = int(input('Digite outro numero: '))


    def subtracao(n1, n2):
        return n1 - n2


    print(subtracao(n1_subtracao, n2_subtracao))

elif chamar_operador == chamar_divisao:
    n1_divisao = int(input('Digite um numero: '))
    n2_divisao = int(input('Digite outro numero: '))


    def divisao(n1, n2):
        return n1 / n2


    print(divisao(n1_divisao, n2_divisao))

elif chamar_operador == chamar_multi:
    n1_multi = int(input('Digite um numero: '))
    n2_multi = int(input('Digite outro numero: '))


    def multi(n1, n2):
        return n1 * n2


    print(multi(n1_multi, n2_multi))

else:
    print('Tente novamente')
