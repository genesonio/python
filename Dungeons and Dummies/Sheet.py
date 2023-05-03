from Ex113 import isInt

pers = {'Nome': '', 'Raça': '', 'Classe': '', 'Alinhamento': '', 'Level': 0, 'Xp': 0, 'Iniciativa': 0,
        'Força': 0, 'Destreza': 0, 'Constituição': 0, 'Inteligência': 0, 'Sabedoria': 0, 'Carisma': 0,
        'Desvantagens': [], 'Idiomas': []}

for i in pers:
    if i == 'Level' or 'Xp' or 'Iniciativa' or 'Força' or 'Destreza' or 'Constituição' or 'Inteligência' or 'Sabedoria' or 'Carisma':
        isInt(f'{i}: ')
    else:
        pers[i] = input(f'{i}: ')

print(pers)

personagens = open(f'{pers["Nome"]}.txt', 'w', encoding='utf-8')
