dados = []
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) # Pedro
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1]) # ['Maria', 19] print(*pessoas[1], sep=', ') = Maria, 19

teste = []
teste.append('Genésio')
teste.append(23)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 12
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera) # tudo
print(galera[2][1]) # 13
for p in galera:
    print(f'{p[0]} tem tantos {p[1]} anos de idade')