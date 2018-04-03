import requests
import json
import sys
while True:
    ILS = 2
    #Ccoinmarketcap#
    dataBTCcoinmarketcap = json.loads(requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=ILS&limit=1").text)
    dataETHcoinmarketcap = json.loads(requests.get("https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=ILS&limit=1").text)
    dataLTCcoinmarketcap = json.loads(requests.get("https://api.coinmarketcap.com/v1/ticker/litecoin/?convert=ILS&limit=1").text)
    dataXRPcoinmarketcap = json.loads(requests.get("https://api.coinmarketcap.com/v1/ticker/Ripple/?convert=ILS&limit=1").text)

    #coinbase#
    dataBTCcoinbase = json.loads(requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy").text)
    dataBTCcoinbase = (dataBTCcoinbase['data']['amount'])
    dataBTCcoinbaseILS = (ILS)
    dataETHcoinbase = json.loads(requests.get("https://api.coinbase.com/v2/prices/ETH-USD/buy").text)
    dataETHcoinbase = (dataETHcoinbase['data']['amount'])
    dataETHcoinbaseILS = (ILS)
    dataLTCcoinbase = json.loads(requests.get("https://api.coinbase.com/v2/prices/LTC-USD/buy").text)
    dataLTCcoinbase = (dataLTCcoinbase['data']['amount'])
    dataLTCcoinbaseILS = (ILS)

    #gemini#
    dataBTCgemini = json.loads(requests.get("https://api.gemini.com/v1/symbols/btcusd").text)

    #print (dataBTCgemini)
    Exchange = ['coinmarketca', 'coinmarketca', 'coinmarketca', 'coinmarketca', 'coinbase', 'coinbase', 'coinbase']
    Coin = [dataBTCcoinmarketcap[0]['symbol'], dataETHcoinmarketcap[0]['symbol'], dataLTCcoinmarketcap[0]['symbol'], dataXRPcoinmarketcap[0]['symbol'], 'BTC', 'ETH', 'LTC']
    Volume = [333.05, 10, 22, 102, 102, 102, 102]
    ILS = [dataBTCcoinmarketcap[0]['price_ils'], dataETHcoinmarketcap[0]['price_ils'], dataLTCcoinmarketcap[0]['price_ils'], dataXRPcoinmarketcap[0]['price_ils'], dataBTCcoinbaseILS, dataETHcoinbaseILS, dataLTCcoinbaseILS]

    Dollar = [dataBTCcoinmarketcap[0]['price_usd'], dataETHcoinmarketcap[0]['price_usd'], dataLTCcoinmarketcap[0]['price_usd'], dataXRPcoinmarketcap[0]['price_usd'],dataBTCcoinbase,dataETHcoinbase,dataLTCcoinbase]
    #table
    titles = ['Exchange', 'Coin', 'Volume', 'ILS', 'Dollar']
    data = [titles] + list(zip(Exchange, Coin, Volume, ILS, Dollar))

    for i, d in enumerate(data):
        line = '|'.join(str(x).ljust(14) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))
time.sleep(1)
