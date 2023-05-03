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

def Balance(client, asset):
    balance = client.get_asset_balance(asset='BUSD')
    p10 = float(balance['free']) * 0.1
    trans = client.get_recent_trades(symbol=asset, limit=1)
    qnty = (1 * p10)/float(trans[0]['price'])
    qyant_input = (f'{qnty:.5f}')
    return float(qyant_input)
