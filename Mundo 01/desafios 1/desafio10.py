
print('\033[1;32mEsse programa calcula quantos dólares você pode comprar')
d = float(input('\033[1;31mDigite o valor atual do dolar $ '))
e = float(input('\033[1;34mDigite o valor do euro EUR '))
r = float(input('\033[1;30mDigite o valor que você tem na carteira: R$ '))
cd = r/d
ce = r/e
print('\033[1;33mCom {:.2f} Reais você pode comprar $ {:.2f} dolares e {:.2f} euros '.format(r, cd, ce))

