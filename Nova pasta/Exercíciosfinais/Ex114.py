import requests


try:
    site = requests.get('http://pudim.com.br')
except:
    print('Infelizmente não consegui acessar o site.')
else:
    print('\033[1;33mConsegui acessar o site Pudim.com.br\033[m')