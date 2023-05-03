import calendar as cl
yr = int(input('Digite um ano: '))
if cl.isleap(yr):
    print('{}{} é um ano bissexto{}'.format('\033[1;32m', yr, '\033[m'))
else:
    print('{}{} não é um ano bissexto{}'.format('\033[1;31m', yr, '\033[m'))