d = float(input('Qual a distância da sua viagem? '))
print('A sua viagem de {}{}km{}, vai custar R$ {}{}{}'.format('\033[1;32m', d, '\033[m', '\033[1;31m', d*0.5, '\033[m') if d<=200
else 'A sua viagem de {}{}km{}, vai custar R$ {}{}{}'.format('\033[1;32m', d, '\033[m', '\033[1;31m', d*0.45, '\033[m'))