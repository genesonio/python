import random as r
from time import sleep
n = r.randint(0,5)
print('Vou pensar entre um número de 0 a 5, tente adivinhar...')
u = int(input('Qual número eu pensei ? '))
print('Processando...')
sleep(2)
print('Parabéns você {}acertou{}'.format('\033[1;32m', '\033[m') if u == n else 'Que pena, você {}errou{}, era {}'.format('\033[1;31m', '\033[m', n))