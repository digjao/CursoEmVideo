from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[1;30;45mJO\033[m')
sleep(1)
print('\033[1;30;45mKEN\033[m')
sleep(1)
print('\033[1;30;45mPO!\033[m')
print('-='*15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*15)
if computador == 0: # computador jogou PEDRA
     if jogador == 0:
         print('EMPATE')
     elif jogador == 1:
         print('JOGADOR VENCE')
     elif jogador == 2:
         print('COMPUTADOR VENCE')
     else:
         print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
     if jogador == 0:
         print('COMPUTADOR VENCE')
     elif jogador == 1:
         print('EMPATE')
     elif jogador == 2:
         print('JOGADOR VENCE')
     else:
         print('JOGADA INVÁLIDA')
elif computador == 2: # computador jogou TESOURA
     if jogador == 0:
         print('JOGADOR VENCE')
     elif jogador == 1:
         print('COMPUTADOR VENCE')
     elif jogador == 2:
         print('EMPATE')
     else:
         print('JOGADA INVÁLIDA')
