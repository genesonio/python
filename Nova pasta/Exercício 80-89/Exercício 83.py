"""este código contém bugs"""

exp = []
exp = input('Digite sua expressão: ')
if exp.count('(') == exp.count(')'):
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.')