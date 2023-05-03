"""Condições Aninhadas
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
carro.siga()
if carro.esquerda():
    etc.
elif carro.direita():
    etc.
else:
    etc.
carro.pare()

if 1x
elif ?x
else 1x """

n = str(input('Qual é seu nome? ')).title()
if n == 'Genésio':
    print('Que maconheiro bonito!')
elif n == 'Ruan' or n == 'Caio' or n =='William':
    print('Seu nome é de maconheiro.')
elif n == 'Ana Cláudia Jéssica  Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(n))
