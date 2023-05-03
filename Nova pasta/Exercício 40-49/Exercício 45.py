from random import randint
from time import sleep
e = 'EMPATE!'
tw = 'Tesoura corta papel!'
pw = 'Papel embrulha pedra!'
pew = 'Pedra esmaga tesoura!'
jw  = 'O jogador venceu!'
cw = 'O computador venceu!'
x = randint(0, 2)
list = ['Pedra', 'Papel', 'Tesoura']
j = str(input('Pedra, papel ou tesoura? ')).strip().title()
sleep(0.5)
print('-='*12)
print(f'O jogador escolheu {j}')
print(f'O computador escolheu {list[x]}')
print('-='*12)
if x == 0 and j == 'Pedra':
    print(e)
elif x == 0 and j == 'Papel':
    print(pw)
    print(jw)
elif x == 0 and j == 'Tesoura':
    print(pew)
    print(cw)
elif x == 1 and j == 'Pedra':
    print(pw)
    print(cw)
elif x == 1 and j == 'Papel':
    print(e)
elif x == 1 and j == 'Tesoura':
    print(tw)
    print(jw)
elif x == 2 and j == 'Pedra':
    print(pew)
    print(jw)
elif x == 2 and j == 'Papel':
    print(tw)
    print(cw)
elif x == 2 and j == 'Tesoura':
    print(e)
else:
    print('Digite uma opção válida')