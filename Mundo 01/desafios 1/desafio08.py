num = int(input('\033[1;30mDigite o valor da medida em metros: '))
print('\033[1;31mMedida em kilômetros {} Km'.format(num/1000))
print('\033[1;32mMedida em hequitômetros {} hc'.format(num/100))
print('\033[1;33mMedida em decâmetros {} dc'.format(num/10))
print('\033[1;34mMedida em metros {} m'.format(num))
print('\033[1;35mMedida em decímetros {} dc'.format(num*10))
print('\033[1;36mMedida em centimetros {} cm'.format(num*100))
print('\033[1;37mMedida em milímetros {} mm'.format(num*1000))
#print('Distância em metros {} m, distância em centímetros {} cm, distância em milíletros {} mm'.format(num, num*100, num*1000))