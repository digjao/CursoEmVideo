'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenuza vai medir {}'.format(hi))'''

from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjavente:'))
hi = hypot(co, ca)
print('A hipotenuza vai medir {}'.format(hi))
