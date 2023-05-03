v = int(input('Qual a velocidade do carro ? '))
if v <= 80:
    print('Você está dentro dos limites, {}parabéns{}'.format('\033[1;32m', '\033[m'))
else:
    print('Você foi multado em {}R$ {}{}, por ultrapassar {}{}Km/h{}'.format(
        '\033[1;31m', (v-80)*7, '\033[m', '\033[1;31m', v-80, '\033[m'
    ))