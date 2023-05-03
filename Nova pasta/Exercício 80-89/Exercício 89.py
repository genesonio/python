historico  = []
dados = []
nome = []
nota = []
while True: # Cria uma lista composta, separando o nome e as notas de cada aluno
    nome.append(str(input('Nome: ')).capitalize())
    dados.append(nome[:])
    nome.clear()
    for c in range(0, 2):
        nota.append(float(input(f'Nota {c+1}: ')))
    dados.append(nota[:])
    nota.clear()
    historico.append(dados[:]) # Copia os dados para o historico
    dados.clear() # limpa os dados
    r = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while r not in 'sn':
        r = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if r == 'n':
        break
for idx, nome in enumerate(historico): # Cria o boletim  com todos os alunos
    if idx == 0:
        print(f'{"ID":<4} | {"NOME":<20} | {"MÉDIA":>6} |')
        print('-'*38)
    media = (historico[idx][1][0] + historico[idx][1][1]) / 2
    print(f'{idx:<4} | {f"{historico[idx][0][0]}":<20} | {media:>6.1f} |')
print('-'*38)
print
while True: # Menu para verificar cada aluno separadamente
    id_aluno = int(input('ID do aluno ou -1 para sair: '))
    while id_aluno > len(historico) - 1 and id_aluno > 0:
        print('Informe o ID correto.')
        id_aluno = int(input('ID do aluno ou -1 para sair: '))
    if id_aluno < 0:
        break
    print('-'*38)
    print(f'Aluno: {historico[id_aluno][0][0]}\nNotas: ', end='')
    print(*historico[id_aluno][1], sep=' | ')
    print('-'*38)
print('-'*38)
print('Volte sempre !')
