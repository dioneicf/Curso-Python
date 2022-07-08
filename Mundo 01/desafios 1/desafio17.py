from math import hypot

co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('Cateto oposto = {} Cateto Adjacente = {} Hipotenusa = {}'.format(co, ca, hi))