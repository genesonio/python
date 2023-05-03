from time import sleep
pt = int(input('Digite o primero termo de uma P.A: '))
r = int(input('Digite a razão da P.A: '))
termo = pt
cont = 1
total = 0
mais = 10
print('Os 10 primeiros termos dessa P.A são:')
sleep(0.3)
while mais != 0:
    total += mais
    while cont <= total:
        print(pt, end=' ')
        pt += r
        cont += 1
    mais = int(input('\nQuantos mais termos você gostaria de ver ?'))
    print('0 para sair')
print(f'Sua P.A foi encerrada com {total} termos')
print('Obrigado')
