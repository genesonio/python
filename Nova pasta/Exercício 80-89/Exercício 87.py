lista = [[],[],[]]
sum_even = sum_terc_c = 0
for c in range (0, 3):
    for y in range (0, 3):
        lista[c].append(int(input(f'Digite um valor para [{c}, {y}]: ')))
print('-='*25)
for x in range (0, 3):
    for y in range (0, 3):
        print(f'[ {lista[x][y]:^5} ]', end='')
    print()
print('-='*25)
for b in lista:
    for n in b:
        if n % 2 == 0:
            sum_even += n
print(f'A soma dos valores pares é: {sum_even}.')
for c in range(0, 3):
    sum_terc_c += lista[c][2]
print(f'A soma dos valores da terceira coluna é: {sum_terc_c}.')
print(f'O maior valor da segunda linha é {max(lista[1])}.')
