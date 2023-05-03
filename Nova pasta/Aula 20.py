def Mensg(x):
    print('-'*30)
    print(f'{x:^30}')
    print('-'*30)


Mensg('CURSO EM VÍDEO')
Mensg('APRENDA PYTHON')
Mensg('GUSTAVO GUANABARA')

def soma(a, b):

    s = a + b
    print(s)


#programa principal
soma(b=4, a=5)

def contador(*num):
    print(f'Você digitou {len(num)} números')


contador(2, 3, 4, 5)
def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
def soma (*n):
    s = 0
    for num in n:
        s += num
    print(s)

soma(2, 3, 4, 5, 1, 2, 5, 2)