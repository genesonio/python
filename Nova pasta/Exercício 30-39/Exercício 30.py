n = int(input('Digite um número: '))
print('O número {}{}{} é par.'.format('\033[1;31m', n, '\033[m') if n % 2 == 0
else 'O número {}{}{} é ímpar.'.format('\033[1;32m', n, '\033[m'))