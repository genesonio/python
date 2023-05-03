c = input('Digite o nome de uma cidade: ')
cm = c.upper().split()
cores = {
    'limpa':'\033[m',
    'VermB':'\033[1;31m',
    'VerdB':'\033[1;32m'
}
if 'SANTO' in cm[0]:
    print('{}Sim{} a cidade começa com Santo'.format(cores['VerdB'], cores['limpa']))
else :
    print('A cidade {}não{} começa com Santo'.format(cores['VermB'], cores['limpa']))