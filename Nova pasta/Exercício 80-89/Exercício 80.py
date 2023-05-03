numeros = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Adicionado ao final da lista')
    else:    
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-'*53)
print(f'Os números digitados foram ordenados {numeros}')
print('-'*53)

# minha solução
"""        if num < numeros[0]:
            numeros.insert(0, num)
            print('Adicionado na posição 0')
        elif numeros[0] < num <= numeros[1]:
            numeros.insert(1, num)
            print('Adicionado na posição 1')
        elif numeros[1] < num <= numeros[2]:
            numeros.insert(2, num)
            print('Adicionado na posição 2')
        elif numeros[2] < num <= numeros[3]:
            numeros.insert(3, num)
            print('Adicionado na posição 3')"""


