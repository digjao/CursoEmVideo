from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
        print('''        [ 1 ] somar 
        [ 2 ] muultiplicador
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        opção = int(input('Qual é a sua opção? '))
        if opção == 1:
            print('A soma dos valores {} e {} é {}'.format(n1,n2(n1+n2)))
        elif opção == 2:
            multi = n1*n2
            print('A multiplicação dos valores {} e {} é {}!'.format(n1,n2,multi))
        elif opção == 3:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print('Entre {} e {}, o maior número é o {}'.format(n1,n2,maior))
        elif opção == 4:
            print('Informe os números novamente!')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
        elif opção == 5:
            sleep(2)
            print('Finalizando')
        else:
            print('Opção inválida')
        print('=-=' *10)
print('Fim do programa! Volte sempre')