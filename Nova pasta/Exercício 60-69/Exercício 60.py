from time import sleep
n = int(input('Digite um valor para fatorar: '))
m = n
f = 1
print(f'Calculando {n}! = ', end='')
while m > 0:
    print(m, end='')
    print(' x 'if m > 1 else ' = ', end='')
    f *= m
    m -= 1
print(f, end='')
sleep(0.2)