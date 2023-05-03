n = int(input('Digite um número: '))
t = 0
for c in range(1, n+1):
    if n % c ==0:
        print('\033[32m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisível {t} vezes.')
if t == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é um número primo.')






"""if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 or n == 3 or n == 5 or n == 7: 
    print(f'O número {n} é um número primo.')
elif n == 2:
    print(f'O número {n} é o único número par, que também é primo.')
else:
    print(f'O número {n} não é um número primo.')"""