jogadores = []
jogador = {"nome": '', "abates":[], "total": 0}
abates = []
while True: # Capta os dados
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    q = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for j in range(0, q): # Pega a quantia de partidas
        abates.append(int(input(f'Quantos abates na partida {j+1}? '))) # Adiciona os abates a lista de abates
    jogador['total'] = sum(abates) # Soma o total de abates
    jogador['abates'] = abates[:] # Faz uma cópia da lista abates para o dicionário Jogador
    jogadores.append(jogador.copy()) # Copia o dict jogador para a lista jogadores
    abates.clear() # Limpa a listade abates
    while True: # Verifica resposta sobre continuar
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if r in 'SN':
            break        
        print('Opção inválida.')
    if r == 'N': # Encerra
        break 
for idx, k in enumerate(jogadores): # Cria a tabela com todos os jogadores
    if idx ==  0:
        print(f'{"ID":<4} | {"NOME":<15} | {"ABATES":<15} | {"TOTAL":<3}')
        print('-'*60)
    print(f'{idx:<4} | {jogadores[idx]["nome"]:<15} | {jogadores[idx]["abates"]} | {jogadores[idx]["total"]:<3}')
while True: # Menu interativo para pegar detalhes de cada jogador isolado
    id_jogador = int(input('ID do player ou -1 para sair: '))
    while id_jogador > len(jogadores) -1 and id_jogador > 0: # Verifica se o ID digitado pertence de fato a algum jogador
        print('Informe o ID correto.')
        id_jogador = int(input('ID do player ou -1 para sair: '))
    if id_jogador < 0:
        break
    print('-'*60)
    print(f'Jogador: {jogadores[id_jogador]["nome"]}\nAbates: ', end='')
    print(*jogadores[id_jogador]["abates"])
    print(f'Total de abates: {jogadores[id_jogador]["total"]}')
