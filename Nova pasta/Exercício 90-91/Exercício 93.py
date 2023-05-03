jogador = {}
abates = []
jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
q = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(0, q):
    abates.append((input(f'Quantos abates na partida {p+1}? ')))
jogador['abates'] = abates[:]
jogador['total'] = sum(abates)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O {k} tem o valor {v}')
print('-='*30)
print(f'O player {jogador["nome"]} jogou {q} partidas.')
for x in range(0, q):
    print(f'    => Na partida {x+1}, realizou {jogador["abates"][x]} abates')
print(f'Com um total de {jogador["total"]} abates.')
