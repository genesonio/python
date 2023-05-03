pessoas = []
pessoa = {}
while True:
    pessoa['Nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['idade'] = int(input('Idade: '))
    pessoa['peso'] = float(input('Peso: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    r = str(input('Deseja continuar? ')).strip().lower()[0]
    while r not in 'sn':
        print('Resposta inválida')
        r = str(input('Deseja continuar[S/N]? ')).strip().lower()[0]
    if r == 'n':
        break
    elif r == 's':
        True
for p in pessoas:
    for k, v in p.items():
        print(f'{k} {v}, ', end='')
    print()