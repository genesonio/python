from random import randint
cont = 0
print('Par ou ímpar de 0 a 10')
print('-'*25)
while True:
    c = randint(0, 10)
    j = int(input('Digite um valor: '))
    s = c + j
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? ')).upper().strip()[0]
    print('Deu PAR' if s % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if s % 2 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu')
            break
    if tipo == 'I':
        if s % 3 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu')
            break
    print('~'*25)
    print('Vamos jogar novamente!')
print('~'*25)
print(f'Você venceu {cont} rodadas.')

"""    if parouimpar == 'p':
        print('Par')
        j = int(input('Digite um número de 0 a 10: '))
        s = c + j
        if s % 2 == 0:
            True
        else:
            break
    elif parouimpar == 'i':
        print('Ímpar')
        j = int(input('Digite um número de 0 a 10: '))
        s = c + j
        if s % 3 == 0:
            True
        else:
            break
        cont += 1
print(f'Você venceu {cont} vezes seguidas')"""

