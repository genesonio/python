mlr_mnr = 0
si = 0
nh = ''
v = 0
for c in range(1, 6):
    print(f'---- {c}ª PESOA ----')
    n = str(input('Nome: ')).strip().title()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().lower()
    if s == 'f':
        if i < 20:
            mlr_mnr += 1
    elif s == 'm' and i > v:
        v = i
        nh = n
    si += i
print(f"""A média de idade entre essas pessoas é: {si/5}.
Existem {mlr_mnr} mulheres menores de 20 anos,
O nome do homem mais velho é {nh} e ele tem {v} anos.""")
