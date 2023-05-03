def escreva(txt):
    v = len(txt) + 2
    print('~'*v)
    print(f'{f"{txt}":^{v}}')
    print('~'*v)

# Programa Principal
escreva(str(input('Digite seu texto: ')))