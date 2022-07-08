from typing import TYPE_CHECKING



R = float(input('Digite o valor do raio: '))
A = 2 * 3.14 * R

if (R > 0):
    print(A)
else:
    print('Digite um valor positivo.')
    
