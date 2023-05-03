from Ex113 import *

cores = ('\033[m',     # 0 -> limpa
         '\033[1;31m', # 1 -> Vermelho
         '\033[1;36m', # 2 -> Azul
         '\033[1;32m', # 3 -> Verde
         '\033[1m', # 4 -> Negrito
         '\033[1;33m', # 5 -> Amarelo
         )


def linha(t=42):
    print(f'{cores[4]}-{cores[0]}'*(t))


def tit(txt):
    linha()
    print(f'{cores[3]}{txt.center(42)}{cores[0]}')
    linha()


def theMenu(lista):
    tit('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'{cores[5]}{c}{cores[0]} - {cores[2]}{i}{cores[0]}')
        c += 1
    linha()
    opc = isInt(f'{cores[5]}Sua Opção:{cores[3]} ')
    print(cores[0])
    return opc
