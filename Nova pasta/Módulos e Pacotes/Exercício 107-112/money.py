def resumo(n, a, d): # EXERCÍCIO 110
    print('-'*35 + f'\n{"  RESUMO DOVALOR ":^35}\n' + '-'*35)
    print(f'Preço analisado: \t{format(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'{a}% de aumento: \t{aumentar(n, a)}')
    print(f'{d}% de redução: \t{diminuir(n, d)}')
    print('-'*35)


def aumentar(n, a, f=True):
    aum = n * (1+(a/100))
    return format(aum) if f == True else aum # Aumenta n em a%

def diminuir(n, d, f=True):
    dim = n * (1-(d/100))
    if f == True: # Modificações do exercício 109
        return format(dim)
    else:
        return dim # Diminui n em d%

def dobro(n, f=True):
    if f == True: # Modificações do exercício 109
        return format(n)
    else:
        return n*2 # Retorna o dobro do valor

def metade(n, f=True):
    if f == True: # Modificações do exercício 109
        return format(n)
    else:
        return n/2 # Retorna metade de n

# V Modificação Ex 108 V
def format(n):
    return f'${n:.2f}'.replace('.', ',') # Retorna n formatado