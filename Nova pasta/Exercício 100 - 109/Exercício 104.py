def isInt(perg):
    while True:
        i = input(perg)
        if i.isnumeric():
            print(f'Você digitou o número {i}')
            break
        else:
            print('\033[1;31mERRO! Digite apenas valores inteiros!\033[m')


 # Programa Principal
n = isInt('Digite um número: ')