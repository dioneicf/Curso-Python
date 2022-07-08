R = float(input('Digite o valor do raio do circulo: '))
A = 2 * 3.14 * R
if (R > 0):
    print('A área do circulo de raio {} é {}'.format (R, A))  
else:
    print('Raio não pode ser nulo ou negativo.')
    