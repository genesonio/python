from time import sleep


cores = ('\033[m',     # 0 -> limpa
         '\033[1;31m', # -> 1 Vermelho
         '\033[1;36m', # -> 2 Azul
         '\033[1;32m') # -> 3 Verde

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')
#
def pyHelp():
    fun = ' '
    while fun.lower() not in 'fim':
        titulo('SISTEMA DE AJUDA PyHELP', 1)
        fun = input('Função ou Biblioteca > ').strip()
        sleep(0.2)
        if fun.lower() == 'fim':
            break
        else:
            titulo(f'  Acessando o manual do comand {fun}', 2)
            sleep(0.3)
            print(cores[3])
            help(fun)
            print(cores[0])
        sleep(0.4)

#Programa Principal
pyHelp()