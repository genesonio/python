grupo = []
pessoa = {"Nome": '', "Sexo": '', "Idade": ''}
totid = 0
while True:  # Coleta de dados
    pessoa['Nome'] = str(input('Nome: ')).title().strip()
    while True: # Mantém em um loop caso opção inválida
        pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper().strip()[0]
        if pessoa['Sexo'] in 'MF': # Verifica se a opção é válida
            break
        print('Opção inválida.')
    pessoa['Idade'] = int(input('Idade: '))
    totid += pessoa['Idade'] # Soma todas as idades
    grupo.append(pessoa.copy()) # Adiciona a pessoa para o grupo
    pessoa.clear() # Limpa pessoa
    while True: # Mantém loop caso opção inválida
        r = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
        if r in 'SN': # Verifica se a opção é válida
            break
        print('Opção inválida.')
    if r == 'N':
        break
med = totid / len(grupo)  # Faz a média da idade
print(f'''- O grupo tem {len(grupo)} pessoas. 
- A média de idade é de {med} anos.
- As mulheres cadastradas são: ''', end='') # Printa informações na tela
for p in grupo: # Lista as mulheres do grupo
    if p['Sexo'] == 'F': # Verifica se são mulheres
        print(f"{p['Nome']} ", end='')
print('\n- Lista das pessoas que estão acima da média de idade:')
for p in grupo: # Lista as pessoas com idade superior a média de idade
    if p['Idade'] > med: # Verifica a idade
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
