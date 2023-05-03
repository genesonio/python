from time import sleep
def linha():
    print('-'*40)
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p == 0:
        p = 1
    if i < f:
        for c in range (i, f+1, p):
            print(f'{c} ', end='', flush=True)
            sleep(0.3)
    if p < 0:
        for c in range(i, f-1, p):
            print(f'{c} ', end='', flush=True)
            sleep(0.3)
    for c in range(i, f-1, -p):
            print(f'{c} ', end='', flush=True)
            sleep(0.3)
    print('FIM!')
    linha()


# Programa Principal
linha()
contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Inicio: '))
f = int(input("Fim: "))
p = int(input('Passo: '))
contador(i, f, p)
