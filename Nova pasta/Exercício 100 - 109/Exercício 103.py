def ficha(name='<desconhecido>', gol=0):
    print(f'O jogador {name} fez {gol} gols no campeonato')

# Programa Principal
n = str(input('Nome do Jogador: ')).capitalize().strip()
g = input('Número de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
