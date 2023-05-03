atv = 1
inv = int(input('Valor: '))
qtd = int(input('Fatiamento: '))
porc = 0.25
tottax = totfat = 0
for c in range(0, qtd):
    atv -= (atv*0.1)
    btc_atual = (inv * porc) + inv
    balance = atv * btc_atual
    fat = balance * 0.1
    totfat += fat
    tax = fat * 0.05
    tottax += tax
    porc += 0.25
print(balance)
print(f'Total fatiamento bruto: {totfat}')
print(f'Total tax: {tottax}')
print(f'Total liq: {totfat - tottax}')
