nome = (input('\033[1;30mDigite o nome do aluno: '))
n1 = float(input('\033[1;31mDigite a primeira nota: '))
n2 = float(input('\033[1;32mDigite a segunda nota: '))
media = ((n1+n2)/2)
print('\033[1;33mA média do aluno {} é {:.1f}'.format(nome, media))