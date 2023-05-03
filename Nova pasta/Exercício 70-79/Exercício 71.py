v = int(input('Digite um valor inteiro para sacar: '))
t = v
ced = 50
totced = 0
while True:
    if t >= ced:
        t -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if t == 0:
            break





# PARTES DO CÓDIGO ANTIGO QUE EU FIZ
"""print(f'''Opções das cédulas de saque:
{n50} notas de R$ 50
{n20} notas de R$ 20
{n10} notas de R$ 10
{n1} notas de R$ 1''')
"""
"""s = n50 = n20 = n10 = n1 = 0"""
"""while s < v:
    s = n50 + n20 + n1 + n1
    while v >= 50:
        v -= 50
        n50 += 1
    while v >= 20:
        v -= 20
        n20 += 1
    while v >= 10:
        v -= 10
        n10 += 1
    while v > 0:
        v -= 1
        n1 += 1"""
