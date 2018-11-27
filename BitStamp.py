import datetime
import requests, json

from time import sleep


def getBitcoinPrice():
    URL = 'https://www.bitstamp.net/api/v2/ticker_hour/btceur/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print "Error querying Bitstamp API"
def getXRPPrice():
    URL = 'https://www.bitstamp.net/api/v2/ticker_hour/xrpeur/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print "Error querying Bitstamp API"

def getLitecoinPrice():
    URL = 'https://www.bitstamp.net/api/v2/ticker_hour/ltceur/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print "Error querying Bitstamp API"

def getEthereumPrice():
    URL = 'https://www.bitstamp.net/api/v2/ticker_hour/etheur/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print "Error querying Bitstamp API"

while True:
    print datetime.datetime.now()
    print "Your coins are currently worth:"
    print "Bitcoin  - " + str(getBitcoinPrice()) + "/BTC"
    print "Ripple   - " + str(getXRPPrice()) + "/XRP"
    print "Litecoin - " + str(getLitecoinPrice()) + "/LTC"
    print "Ethereum - " + str(getEthereumPrice()) + "/ETH"

    print " "
    sleep(10)


