from random import randint
def sorteio():
    print(f'Sorteando 5 valores para lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n} ', end='')
    print('Fim!')
def som_Par(num):
    sum_par = 0
    for n in num:
        if n % 2 == 0:
            sum_par += n
    print(f'Somando valores pares de {num}, temos {sum_par}')

numeros = []
sorteio()
som_Par(numeros)