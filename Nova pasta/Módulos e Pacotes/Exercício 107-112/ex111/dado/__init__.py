# EXERCÍCIO 112

def isMoney(msg):
    valid = False
    while not valid:
        price = str(input(msg)).strip().replace(',', '.')
        if price.isalpha() or price == '':
            print(f'\033[1;31mERRO! {price} não é um preço válido\033[m')
        else:
            valid = True
            return float(price)