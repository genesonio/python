from random import randint
from time import sleep
from operator import itemgetter
jogo = {f'jogador {c}': randint(1, 6) for c in range(1, 5)}
print('Valores sorteados:')
rank = []
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.3)
print('-='*13)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"RANKING DOS JOGADORES":=^30}')
for i, v in enumerate(rank):
    print(f'{f"{i+1}º lugar: {v[0]} com {v[1]}":_^30}')
    sleep(0.3)
print('-'*30)