def fatorial(n, show=False):
    """-> Calcula o fatorial de um número.
    :param n: Número a ser fatorado
    :param show: (opcional) Define se vai ser mostrado o cálculo ou não
    :return: O valor do fatorial do número 'n'"""
    f = 1
    for c in range (n, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
    return f

print(fatorial(5, show=False))
help(fatorial)