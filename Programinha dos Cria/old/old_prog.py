from time import sleep
from binance.enums import *
from binance.spot import *
from binance.client import Client
from corpo import *
from arquivo import *

kenzo = Client(kk, ksk)
client = Client(k, sk)

price = []
asset = []
while True:
    getOrders(kenzo, asset, price)
    print(asset)
    client_price = []
    opened_orders = []
    getOrders(client, opened_orders, client_price)
    for c in range(0, len(asset)):
        if asset[c] not in opened_orders:
            balance = Balance(client, asset[c])
            client.create_test_order(symbol=asset[c], side=SIDE_BUY,
                                     type=ORDER_TYPE_LIMIT, quantity=balance, timeInForce=TIME_IN_FORCE_GTC,
                                     price=price[c])
            print(f'Aberta ordem {price[c]} {asset[c]}')
        else:
            print('Já existe')
    sleep(600)


