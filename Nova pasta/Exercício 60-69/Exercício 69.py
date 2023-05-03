from time import sleep
toth = p18 = m20 = 0
while True:
    i = int(input('Qual a idade: '))
    s = ' '
    while s not in 'mf':
        s = str(input('Qual o sexo [F/M]: ')).strip().lower()[0]
    if s == 'f' and i < 20:
        m20 += 1
    elif s == 'm':
        toth += 1
    if i >= 18:
        p18 += 1
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar? ')).strip().lower()[0]
    if resp == 'n':
        break
    
print('Computando...')
sleep(0.5)
print(f'''{m20} são mulheres menores de 20 anos.
{p18} são maiores de 18 anos
{toth} são homens.''')