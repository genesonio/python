from random import randint
t = 0
u = 0
n = randint(0, 10)
print('Vou pensar entre um número de 0 a 10, tente adivinhar...')
while u != n:
    u = int(input('Qual sua opção: '))
    t += 1
    if u > n:
        print('Menos...')
    elif u < n:
        print('Mais...')
if t == 1:
    print('Parabéns você {}acertou{} e precisou de {} tentativa'.format('\033[1;32m', '\033[m', t))
else:
    print('Parabéns você {}acertou{} e precisou de {} tentativas'.format('\033[1;32m', '\033[m', t))