numbers = []
while True:
    numbers.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    if resp == 'n':
        break
numbers.sort(reverse=True)
print('-'*38)
print('Lista de números na ordem decrescente: ', end='')
print(*numbers, sep=', ')
print(f'Foram digitados {len(numbers)} números.')
if 5 in numbers:
    if numbers.count(5) > 1:
        print(f'Esta foi a quantidade de números 5: {numbers.count(5)}')
    else:
        print('O número 5 só foi digitado uma vez.')
else:
    print('Não foi digitado nenhuma vez o número 5')