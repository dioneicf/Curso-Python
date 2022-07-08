salario = float(input('Digite o valor do salário do funcionário: '))
aumento = float(input('Digite o percentual do do aumento do salário: '))
total = salario + (salario*aumento/100)
print('Salário atual: R$ {:.2f}\nPercentual do aumento {:.2f} %\nNovo salário: R$ {:.2f}'.format(salario, aumento, total))