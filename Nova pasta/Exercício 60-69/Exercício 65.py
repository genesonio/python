from time import sleep
cont = s = maior = menor = 0
c = ''
while c != 'n':
    cont += 1
    n = int(input(f'Digite o {cont}º número: '))
    s += n
    c = str(input('Quer cotinuar S/N: ')).lower().strip()[0]
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        
m = s / cont
print('CALCULANDO...')
sleep(0.3)
print('-='*15)
print(f"""Você digitou {cont} números.
A média deles é {m:.2f}.
O menor número foi {menor}.
O maior número foi {maior}.""")
print('-='*15)
