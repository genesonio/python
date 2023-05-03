cont = n = s = 0
n = int(input(f'Digite o {cont}º número[999 para parar]: '))
while n !=  999:
    cont += 1
    s += n
    n = int(input(f'Digite o {cont}º número[999 para parar]: '))
print(f'''Você digitou {cont} números.
A soma dos números é {s}''')
