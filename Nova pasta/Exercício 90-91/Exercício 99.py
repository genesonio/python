from time import sleep


def linha():
    print('-='*40)

def maior(*num):
    print('Analisando valores passados ', end='')
    for v in num:    
        print(f"{v} ", flush=True, end='')
        sleep(0.3)
    print(f'\nForam informados {len(num)} valores ao todo.')
    if len(num) > 0:
        print(f"O maior valor foi de {max(num)}.")
    else:
        print('Não houve valor maior, pois não há valor algum.')
    linha()

linha()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()