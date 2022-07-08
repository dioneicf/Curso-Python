print('\033[30mPrograma que calcula a área de uma parade e o consumo de tintar pra pintar.')
alt = float(input('\033[31mDigite o valor da altura da parede: '))
lar = float(input('\033[32mDigite o valor da largura da parede: '))
area = (alt*lar)
tin = (area/2)
print('\033[33mA área da parede é {} m2 que vai utilizar {} litros de tinta'.format(area, tin))


