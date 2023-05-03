def dado():
    """ -> Joga um dado quantas vezes quiser.
    Aceita dado de 2, 4, 6, 8, 10, 12, 20 e 100 lados."""
    from time import sleep
    from random import randint   
    while True:
        sum = 0
        d = int(input('De quantos lados quer o dado? '))
        if d in (2, 4, 6, 8, 10, 12, 20, 100): 
            v = int(input('Quantas vezes quer jogar? '))
            print(f'D{d} = ', end='', flush=True)
            for c in range(0, v):
                re = randint(1, d)
                if c < v-1:
                    sleep(0.4)
                    print(f"{re}, ", end='', flush=True)
                else:
                    print(f'{re}.', flush=True)
                    sleep(0.4)
                sum += re
            sleep(0.4)
            print(f'\033[1;32mTotal: {sum}\033[m', flush=True)
            break
        else:
            print('\033[1;31mDado inválido\033[m')

def create_sheet():
    char = {} # Cria um dicionário com as informações do personagem
    char['name'] = str(input('Nome do personagem: ')).title().strip()
    char['sex'] = str(input('Sexo do personagem[M/F]: ')).upper().strip()[0]
    char['race'] = str(input('Raça do personagem: ')).title().strip()
    char['class'] = str(input('Classe do personagem: ')).title().strip()
    char['str'] = int(input('Força do personagem: '))
    char['dex'] = int(input('Destreza do personagem: '))
    char['con'] = int(input('Constituição do personagem: '))
    char['wisd'] = int(input('Conhecimento do personagem: '))
    char['int'] = int(input('Inteligência do personagem: '))
    char['char'] = int(input('Carisma do personagem:'))
    char['exp'] = 0
    char['lvl'] = 0
    return char
     
     
# Programa Principal   
cat = [] # Um catálogo dos personagens em uma lista
while True:
    pers = create_sheet() # Chama Criação de Pers
    cat.append(pers.copy()) # Copia o pers criado para uma lista
    while True: # Verifica se quer cotinuar
        r = str(input('Quer continuar ?')).upper().strip()[0]
        if r in 'SN': 
            break
        print('Opção inválida.')
    if r == 'N': # interrompe o loop caso não queira continuar
        break

for idx, k in enumerate(cat): # Cria tabela com personagens
    if idx == 0:
        print(f"{'ID':<4} | {'Nome':<15} | {'Raça':<7} | {'Classe':<7} | {'Lvl':<4}")
        print('-'*60)
    print(f"{idx:<4} | {cat[idx]['name']:<15} | {cat[idx]['race']:<7} | {cat[idx]['class']:<7} | 0")

while True: # Menu interativo para verificação do personagem
    char_id = int(input('ID do personagem -1 para sair: '))
    while char_id > len(cat) -1 and char_id > 0:
        print('Informe o ID correto')
        char_id = int(input('ID(-1 para sair): '))
    if char_id < 0:
        break
    print('-'*60)
