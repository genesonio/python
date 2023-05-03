n = input('Digite um número entre 0 e 9999: ')
s = '000' + n
cores = {'limpa':'\033[m',
        'VermB':'\033[1;31m',
        'VerdB':'\033[1;32m',
        'AmaB':'\033[1;33m',
        'AzuB':'\033[1;34m'}

print (f'Unidade:', cores['VermB'], s[-1], cores['limpa'])
print (f'Dezena:', cores['VerdB'], s[-2], cores['limpa'])
print (f'Centena:', cores['AmaB'] ,s[-3], cores['limpa'])
print (f'Milhar:', cores['AzuB'] ,s[-4], cores['limpa'])