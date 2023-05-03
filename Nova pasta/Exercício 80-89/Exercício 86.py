lista = [[],[],[]]
for c in range (0, 3):
    for y in range (0, 3):
        lista[c].append(int(input(f'Digite um valor para [{c}, {y}]: ')))
print('-='*11)
for x in range (0, 3):
    for y in range (0, 3):
        print(f'[{lista[x][y]:^5}]', end='')
    print()
print('-='*11)
