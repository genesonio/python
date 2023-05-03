from interface import *


cores = ('\033[m',     # 0 -> limpa
         '\033[1;31m', # 1 -> Vermelho
         '\033[1;36m', # 2 -> Azul
         '\033[1;32m', # 3 -> Verde
         '\033[1m', # 4 -> Negrito
         '\033[1;33m', # 5 -> Amarelo
         )


def arqExiste(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArq(name):
    a = open(name, 'wt+')
    
    
def lerArq(arch):
    try:
        a = open(arch, 'rt', encoding='UTF-8')
    except:
        print(f'{cores[1]}Falha ao ler o arquivo!{cores[0]}')
    else:
        tit('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close


def cadastrar(arch, name='desconhecido', age=0):
    try:
        a = open(arch, 'a', encoding='UTF-8')
    except:
        print(f'{cores[1]}Houve um ERRO ao abrir o arquivo.{cores[0]}')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print(f'{cores[1]}Houve um ERRO na hora de escrever os dados!{cores[0]}')
        else:
            print(f'{cores[3]}Novo registro de {name} adicionado.{cores[0]}')
            a.close()