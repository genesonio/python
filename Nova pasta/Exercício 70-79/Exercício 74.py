from random import randint
num_ale = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print('Os números foram: ', end='')
for pos, num in enumerate(num_ale):
    print(f'{num} ', end='')
print(f"""\nO maior valor sorteado foi {max(num_ale)}
O menor valor sorteado foi {min(num_ale)}""")
