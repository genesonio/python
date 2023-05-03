n = int(input('Digite o multiplicador: '))
for c in range(1, 11):
    print('\033[1m{} x {} = {}\033[m'.format(c, n, c*n))