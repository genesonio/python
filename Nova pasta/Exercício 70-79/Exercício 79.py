lis = [] # cria a lista
while True:
    a = int(input('Digite um valor: '))
    if a not in lis: # verifica se o valor digitado já está na lisa
        lis.append(a) # adiciona caso não esteja
        print('Número adicionado com sucesso.')
    else:
        print('Número duplicado, não irei adicionar.')
    resp = str(input('Deseja continuar? ')).strip().lower()[0] # pergunta se quer continuar
    if resp == 'n':
        break
lis.sort()
print(f'Você digitou os valores {lis}')
