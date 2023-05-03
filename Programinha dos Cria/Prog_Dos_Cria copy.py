from arquivo import *
from commands import *
from binance.client import Client
from binance.websocket.binance_socket_manager import BinanceSocketManager

# Programa Principal
# API key inf
kClient = Client(kk, ksk)
for c in client_login:
    cClient = Client(c['key'], c['secretkey'], testnet=True)

openTOrder(cClient)





# Programa Testes V

"""
k_Asset = []
k_Price = []
k_Side = []
getOrders(kClient, k_Asset, k_Price0, k_Side)
print(k_Asset, k_Price, k_Side)"""

# (End) Refazer o bot da maneira antiga, melhor escrito, multiplos bots pra verificação de dados e um main bot simples para execução.
# 1 Cancelar ordem do user quando server cancelar
# 2 Fechar ordem, quando a ordem estiver rolando
# 3 Fazer teste de exceções e erros (definir os erros)
#
#
#
# ? Conectar a conta pelo websocket (Provavelmente não)
