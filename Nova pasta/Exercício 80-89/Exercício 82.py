all_num = []
even_num = []
odd_num = []
while True:
    num = int(input('Digite um número: '))
    all_num.append(num)
    resp = str(input('Deseja continuar[S/N]? ')).strip().lower()[0] # pergunta se quer continuar
    if num % 2 == 0:
        even_num.append(num)
    elif num % 2 == 1:
        odd_num.append(num)
    if resp == 'n':
        break
print('Todos os números: ', end='')
print(all_num, sep=', ')
print('Números pares: ', end='')
print(even_num, sep=', ')
print('Números ímpares: ', end='')
print(odd_num, sep=', ')