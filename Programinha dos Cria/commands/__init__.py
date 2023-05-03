from socket import socket
import websocket
import time


# Current timestamp
ts = time.time()
tstamp = str(ts).replace('.', '')


# Função aux
def on_message(ws, message):
    print(message)


def on_close(ws):
    print("Connection closed")


# Array of a candle
def streamKline(client, symbol, interval):
    """Get an Kline in a array with all info

    Args:
        symbol (str): A valid symbol from Binance
        interval (str): A valid interval from Binance API
    """
    socket = f'wss://stream.binance.us:9443/ws/{symbol}@kline_{interval}'
    ws = websocket.WebSocketApp(socket,
                                on_message=on_message,
                                on_close=on_close)


# Test order function
def openTOrder(client):
    """Open a Test Order

    Args:
        client (var): var with key and secret key
    """
    from arquivo import kk, ksk
    from binance.client import Client
    k_Asset = []
    k_Price = []
    k_Side = []
    kClient = Client(kk, ksk, {'verify': True, 'timeout': 1000})
    getOrders(kClient, k_Asset, k_Price, k_Side)
    for order in range(0, len(k_Asset)):
        quantity = Balance(client, k_Asset[order])
        print(f'Min Quantity: {minQuantity(k_Asset[order])}')
        if quantity >= minQuantity(k_Asset[order]):
            client.create_test_order(symbol=k_Asset[order], side='BUY', type='LIMIT',
                                     quantity=quantity, timeInForce='GTC', price=k_Price[order])
            print(f'''Test Order Open:
                asset: {k_Asset[order]}
                price: {k_Price[order]}
                quantity: {quantity}''')
        else:
            print('Quantidade mínima excedida')


# Real order function
def openOrder(client, symbol: str, price: int, side: str, quantity: int):
    """Create a real order on binance

    Args:
        symbol (str): A valid symbol from Binance
        price (flot): A price that set the order
        side (str): A side BUY or SELL the asset
        quantity (float): A quantity of the asset(symbol) that will be exec
    """
    socket = f'https://api.binance.com/api/v3/order/symbol={symbol}&side={side}%type=LIMIT&timeInForce=GTC%quantity={quantity}&price={price}&timestamp={tstamp}'
    ws = websocket.WebSocketApp(socket,
                                on_message=on_message,
                                on_close=on_close)


# All opened orders
def openOrders():
    sokcet = f'https://api.binance.com/api/v3/openOrders'
    ws = websocket.WebSocketApp(socket,
                                on_message=on_message,
                                on_close=on_close)


def accountStatus():
    socket = f'https://api.binance.com//sapi/v1/account/status'
    ws = websocket.WebSocketApp(socket,
                                on_message=on_message,
                                on_close=on_close)


def Balance(client, asset):
    balance = client.get_asset_balance(asset='BUSD')
    p10 = float(balance['free']) * 0.1
    trans = client.get_recent_trades(symbol=asset, limit=1)
    qnty = (1 * p10)/float(trans[0]['price'])
    qyant_input = (f'{qnty:.5f}')
    return float(qyant_input)


def getOrders(client, asset, price, side):
    import json
    open_ord = client.get_open_orders()
    with open('ord_db.json', 'w') as arq:
        json.dump(open_ord, arq)
    with open('ord_db.json', 'r') as arq:
        data = json.load(arq)
        for o in data:
            asset.append(o['symbol'])
            price.append(o['price'])
            side.append(o['side'])


def minQuantity(asset):
    from binance.spot import Spot
    from arquivo import kk, ksk
    log = Spot(kk, ksk)
    resp = log.avg_price(asset)
    price = (resp['price'])
    calc = 10 / float(price)
    min = f'{calc:.7f}'
    return min
