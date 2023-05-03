from time import sleep
print('{:=^40}'.format(' Lojas Pacheco '))
print('Obrigado pela preferência.')
print('-='*20)
p = float(input('Digite o valor do produto: '))
c = int(input("""Formas de pagamento:
1- À vista dinheiro ou cheque.
2- À vista no cartão de crédito.
3- Em 2x no cartão.
4- Em 3x ou mais no cartão.
Condição: """))
print('-='*20)
sleep(0.5)
if c == 1:
    print('Você obteve 10% de desconto.')
    print('O preço ficou em {:.2f}, você economizou {:.2f}'.format(p*0.9, p*0.1))
elif c == 2:
    print('Você obteve 5% de desconto.')
    print('O preço ficou em {:.2f}, você economizou {:.2f}'.format(p*0.95, p*0.05))
elif c == 3:
    print('Não houveram alterações de preço.')
    print(f'Preço total de {p} em duas parcelas de {p/2}')
elif c == 4:
    pa = int(input('Em quantas parcelas: '))
    if pa == 1:
        print('Você obteve 5% de desconto.')
        print('O preço ficou em {:.2f}, você economizou {:.2f}'.format(p*0.95, p*0.05))
    elif pa == 2:
        print('Não houveram alterações de preço.')
        print(f'Preço total de {p} em duas parcelas de {p/2}')
    else:
        print('Houve um acréscimo de 20% em sua compra')
        print('O preço ficou em {:.2f}, em {} prestações de {}'.format(p*1.2, pa, (p*1.2)/pa))
else:
    print('Por favor, digite uma opção válida.')
print('Obrigado pela preferência!')
print('-='*20)