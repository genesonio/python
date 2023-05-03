# Condição v
#if xx.xx():
#    bloco True
#else:
#    bloco False

#tempo = int(input('Quantos anos tem seu carro? '))
#print('Carro novo.'if tempo<=3 else'Carro velho.')
#print('--FIM--')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média é: {m:.1f}')
if m >=7:
    print('Sua média foi boa. parabéns')
elif m >=6:
    print('Você está na média, estude mais.')
else:
    print('Estude mais!')