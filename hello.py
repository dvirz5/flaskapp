from coinbase.wallet.client import Client
client = Client(<api_key>, <api_secret>)

price = client.get_sell_price(currency_pair = 'BTC-USD')
