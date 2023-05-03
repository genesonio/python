def area(l, a):
    are = l * a
    print(f'A área de um terreno de {l}m x {a}m é {are}m².')

# Programa Principal
print(f'{f"Controle de Terrenos":^50}')
print('='*50)
n1 = float(input('LARGURA (m): '))
n2 = float(input('ALTURA (m): '))
area(n1, n2)
print('='*50)
