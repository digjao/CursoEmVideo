#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
contmaior = 0
cont = 0
for c in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    atual = date.today().year - ano
    if atual >= 18:
        cont += 1
    else:
        contmaior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont))
print('E também tivemos {} pessoas menores de idade '.format(contmaior))