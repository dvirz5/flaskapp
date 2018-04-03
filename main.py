from flask import Flask
from flaskext.mysql import MySQL
from flask import Flask,request
import requests
import json
import sys
from flask import render_template
import gdax
import gemini
import urllib.request as urllib2

#public_client = gdax.PublicClient()

# gdax
    #publicClient = gdax.PublicClient(product_id="ETH-USD")
    #what = public_client.get_product_historic_rates('ETH-USD')
    #gdaxBTC = (what)
    #public_client = gdax.PublicClient()
    #print (gdaxBTC)

app = Flask(__name__)

VerifyAccountStatus = True
name = "btc"
@app.route('/coin/')

@app.route('/coin/<name>')

def hello(name=name):
    
    #floatrates ILS VALUE
    datafloatrates = json.loads(requests.get("http://www.floatrates.com/daily/usd.json").text)
    datafloatratesILS = (datafloatrates['ils']['rate'])
    ILSvalue = datafloatratesILS

    if name == 'btc':
       namee = 'bitcoin'
    elif name == 'ltc':
        namee = 'litecoin'
    elif name == 'ETH':
        namee = 'ethereum'
    print (name)
    
    #Ccoinmarketcap#
    datacoinmarketcap = json.loads(requests.get("https://api.coinmarketcap.com/v1/ticker/" + namee + "/?convert=ILS&limit=1").text)
    datacoinmarketcapvalue = float(datacoinmarketcap[0]['price_usd'])
    datacoinmarketcapILS = round((datacoinmarketcapvalue * ILSvalue), 4)
    #print (datacoinmarketcapILS )
    #gemini#
    base_url = "https://api.gemini.com/v1"

    response = urllib2.urlopen(base_url + "/symbols")
    #print(response.read())
    #coinbase#
    datacoinbase = json.loads(requests.get("https://api.coinbase.com/v2/prices/" + name.upper() + "-USD/buy").text)
    datacoinbase = float(datacoinbase['data']['amount'])
    datacoinbaseILS = round((datacoinbase * ILSvalue), 4)
    #print (datacoinbaseILS )

 
    #Gatehub
    

    #table start!
    Exchange = ['coinmarketca', 'coinbase', 'gemini', 'Gatehub', 'gdax']
    Volume = [ '+++', '+++', '+++', '+++', '+++']
    #Volume.sort()
    ILS = [datacoinmarketcapILS, datacoinbaseILS, '+++', '+++', '+++']
    Dollar = [datacoinmarketcap[0]['price_usd'], datacoinbase, '+++', '+++', '+++']
   
    #Dollar.sort()
    FrontPrice = datacoinbase
    invisimabuyprice = (Dollar[0])
    
    print ('COOL ! ' + invisimabuyprice + ' choose by script')
    titles = ['Exchange', 'Volume', 'ILS', 'Dollar']
    data = [titles] + list(zip(Exchange, Volume, ILS, Dollar))
    for i, d in enumerate(data):
        line = '|'.join(str(x).ljust(15) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))
    coin = name
    #print (invisimabuyprice)
    #i = invisimabuyprice
   


    #closedeal = Dollar[0] * 1.5
   

    return render_template('coin.html', name=name, FrontPrice=FrontPrice, invisimabuyprice=invisimabuyprice)
     
@app.route('/wallet/')  
@app.route('/wallet/<name>')
def wallet(name=None):
  return render_template('wallet.html', VerifyAccountStatus=VerifyAccountStatus, name=name)

if __name__ == "__main__":
    app.run()
