listanum = []
for c in range (0, 5):
    listanum.append((input(f'Digite um número para a posição {c}: ')))
print('-'*40)
print(f'Você digitou os números: ', end='')
print(*listanum, sep=', ')
print(f'O maior valor digitado foi {max(listanum)} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == max(listanum):
        print(f'{i}, ', end='')
print(f'\nO menor valor digitado foi {min(listanum)} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == min(listanum):
        print(f'{i}, ', end='')
