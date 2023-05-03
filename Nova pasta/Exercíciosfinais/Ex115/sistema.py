from interface import *
from dados import *
from time import sleep

arq = 'Exercíciosfinais\Ex115\pessoas.txt'
if not arqExiste(arq):
    criarArq(arq)

cores = ('\033[m',     # 0 -> limpa
         '\033[1;31m', # 1 -> Vermelho
         '\033[1;36m', # 2 -> Azul
         '\033[32m', # 3 -> Verde
         '\033[1m', # 4 -> Negrito
         '\033[1;33m' # 5 -> Amarelo
         )

while True:
    resp = theMenu(['Cadastrar Pessoa', 'Pessoas Cadastradas', 'Sair do Programa'])
    if resp == 1:
        tit('Cadastrar Pessoa')
        n = str(input('Nome: '))
        i = isInt('Idade: ')
        cadastrar(arq, n, i)
    elif resp == 2:
        lerArq(arq)
    elif resp == 3:
        print(f'{cores[3]}Volte sempre!{cores[0]}')
        break
    else:
        print(f'{cores[1]}ERRO! Digite uma opção válida.{cores[0]}')
    sleep(1)