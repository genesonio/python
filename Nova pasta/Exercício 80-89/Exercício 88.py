from random import randint
from time import sleep
lista = []
jogos = []
print('-'*40)
print(f'{"Joga na Mega Sena":^40}')
print('-'*40)
q = int(input('Quantos jogos você quer que eu sorteie? ')) # Coleta a quantia de jogos
for c in range(0, q): # Rola a quantia de vezes
    while len(jogos) < 6: # Enquanto não tiverem 6 números, fica num loop infinito
        num = randint(1, 61)
        if num not in jogos: # Verifica se o número sorteado já está naquele jogo
            jogos.append(num)
    jogos.sort()
    lista.append(jogos[:]) # Passa o jogo para a lista de jogos
    jogos.clear() # Limpa o "Cache"
for c in range(0, q): # Printa as informações na tela c/ delay de 0.3s
    print(f'Jogo {f"{c+1} ->":<3}|{f"{lista[c]}":_^30}|')
    sleep(0.3)
