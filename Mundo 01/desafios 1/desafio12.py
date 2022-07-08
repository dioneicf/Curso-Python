v = float(input('Digite o valor do produto: '))
d = float(input('Digite a porcentagem do desconto: '))
t = v - (v*d/100)
print('Valor do produto {:.2f}, valor do desconto {:.2f} %, valor total = {:.2f}'.format(v, d, t))