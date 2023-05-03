from binance.client import Client
from arquivo import *
import pandas as pd
import json


client = Client(api_key=k, api_secret=sk)

assets = ['BTCUSDT']


def dfDownload(client):
    """Uma função que pesquisa uma lista de preços na binance
    Args:
        client (str): Um dos pares aceitos pela API da Binance ex('BTCUSDT')
    """
    for a in assets:
        hist = client.get_historical_klines(
            symbol=a, interval=Client.KLINE_INTERVAL_30MINUTE, start_str=0)
        var = a+'_df'
        with open(var+'.json', 'w') as e:
            json.dump(hist, e)
        for line in hist:
            del line[:5]
        var = pd.DataFrame(
            hist, columns=['date', 'open', 'high', 'low', 'close'])
        var.set_index('date', inplace=True)
        var.index = pd.to_datetime(var.index, unit='ms')
        var['close'] = pd.to_numeric(var['close'])
        ema8 = var['close'].ewm(span=2688).mean()


dfDownload(client)

