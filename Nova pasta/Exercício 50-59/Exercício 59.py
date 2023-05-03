from time import sleep
o = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while o != 5:
    sleep(0.3)
    o = int(input("""[1] Somar.
[2] Multiplicar.
[3] Maior.
[4] Novos Números.
[5] Sair.
------------------
>>>> """))
    if o == 1:
        sleep(0.5)
        print(f'{n1} + {n2} = {n1 + n2}')
        print('-'*18)
    elif o == 2:
        sleep(0.5)
        print(f'{n1} x {n2} = {n1 * n2}')
        print('-'*18)
    elif o == 3:
        sleep(0.5)
        if n1 > n2:
            print(f'{n1} é maior')
            print('-'*18)
        elif n2> n1:
            print(f'{n2} é maior')
            print('-'*18)
        else:
            print('São o mesmo número')
            print('-'*18)
    elif o == 4:
        sleep(0.5)
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print('-'*18)
    elif o == 5:
        sleep(0.1)
        print('Obrigado, volte sempre!')
    else:
        sleep(0.7)
        print('Opção inválida.')
print('Você saiu.')