pessoas = [[], []]
maipes = menpes = 0
nom_pes = nom_lev = ''
while True:
    pessoas[0].append(str(input('Nome: ')))
    pessoas[1].append(float(input('Peso: ')))
    r = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    while r not in 'sn':
        r  = str(input('Deseja continuar ?')).strip().lower()[0]
    if r == 'n':
        break
print(f'Foram cadastradas {len(pessoas[0])} pessoas')
for c, p in enumerate(pessoas[1]):
    if c == 0:
        maipes = menpes = p
        nom_pes = pessoas[0][c]
    if p > maipes:
        maipes = p
        nom_pes = pessoas[0][c]
    if p < menpes:
        menpes = p
        nom_lev = pessoas[0][c]
print(f'O maior peso é de {maipes:.1f}KG, das pessoas: ', end='')
for c, p in enumerate(pessoas[1]):
    if p == maipes:
        print(f'{pessoas[0][c]}', end=', ')
print(f'\nO menor peso é de {menpes:.1f}KG, das pessoas: ', end='')
for c, p in enumerate(pessoas[1]):
    if p == menpes:
        print(f'{pessoas[0][c]}', end=', ')
