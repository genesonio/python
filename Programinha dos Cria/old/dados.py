from binance.client import Client
from arquivo import *
import pandas as pd
import json
import matplotlib.pyplot as plt


# Loga na conta do cliente pela API key e API Secret Key
client = Client(api_key=k, api_secret=sk)

# Pega os dados do symbol(asset), num intevalo de tempo (interval), são as candlesticks só que sem os gráficos
historical = client.get_historical_klines(
    symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_30MINUTE, start_str=0)

with open('btcusd_df.json', 'w')as e:  # cria um arquivo .json para salvar os dados baixados
    json.dump(historical, e)  # joga os dados dentro do arquivo
for line in historical:
    del line[5:]  # Deleta a linha 5 (Volume)
btcusdt_df = pd.DataFrame(historical, columns=[
                          'date', 'open', 'high', 'low', 'close'])  # Transforma o .json em colunas
btcusdt_df.set_index('date', inplace=True)
# Tira as horas da data, deixando apenas ano-mes-dia
btcusdt_df.index = pd.to_datetime(btcusdt_df.index, unit='ms')
# btcusdt_df['open'] = pd.to_numeric(btcusdt_df['open']) # série de códigos que melhora visualização do .json
# btcusdt_df['high'] = pd.to_numeric(btcusdt_df['high'])
# btcusdt_df['low'] = pd.to_numeric(btcusdt_df['low'])
btcusdt_df['close'] = pd.to_numeric(btcusdt_df['close'])
# plt.xlabel('Tempo')
# plt.ylabel('Preço')
# # plt.plot(btcusd_df['close'], label='close')
# # plt.legend()

ema8 = btcusdt_df['close'].ewm(span=2688).mean()
# plt.plot(ema8, label='EMA')
# plt.title('EMA 8w')
# plt.legend()
print(ema8)
# plt.show()
