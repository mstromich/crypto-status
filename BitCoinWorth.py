import datetime
import requests, json

from time import sleep

#Total amounts of Crypto Currency owned
btcAmount = 0.00457745
xrpAmount = 33.99562195
ltcAmount = 0.28320992
ethAmount = 0.05194469
gamAmount = 9.26232558

#Variable initialization for the stats
btcMaxValue = 0
btcMinValue = 0
xrpMaxValue = 0
xrpMinValue = 0
ltcMaxValue = 0
ltcMinValue = 0
ethMaxValue = 0
ethMinValue = 0
gamMaxValue = 0
gamMinValue = 0

#API calls
def getBitcoinPrice():
    URL = 'https://bitbay.net/API/Public/BTCEUR/ticker.json'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        price_float = priceFloat * btcAmount
        return price_float
    except requests.ConnectionError:
        print("Error querying Bitstamp API")
def getXRPPrice():
    URL = 'https://www.bitstamp.net/api/v2/ticker_hour/xrpeur/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        price_float = priceFloat * xrpAmount
        return price_float
    except requests.ConnectionError:
        print("Error querying Bitstamp API")

def getLitecoinPrice():
    URL = 'https://bitbay.net/API/Public/LTCEUR/ticker.json'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        price_float = priceFloat * ltcAmount
        return price_float
    except requests.ConnectionError:
        print("Error querying Bitstamp API")

def getEthereumPrice():
    URL = 'https://bitbay.net/API/Public/ETHEUR/ticker.json'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        price_float = priceFloat * ethAmount
        return price_float
    except requests.ConnectionError:
        print("Error querying Bitstamp API")

def getGamePrice():
    URL = 'https://bitbay.net/API/Public/GAMEEUR/ticker.json'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        price_float = priceFloat * gamAmount
        return price_float
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


while True:
    print(datetime.datetime.now())
    print("Your coins are currently worth:")
    print("BitCoin  - EUR " + str(getBitcoinPrice()))
    print("XRP      - EUR " + str(getXRPPrice()))
    print("LiteCoin - EUR " + str(getLitecoinPrice()))
    print("Ethereum - EUR " + str(getEthereumPrice()))
    print("Game     - EUR " + str(getGamePrice()))
    print("-----------------------------")
    cryptoTotal = getBitcoinPrice() + getXRPPrice() + getLitecoinPrice() + getEthereumPrice() + getGamePrice()
    print("Total    - EUR",cryptoTotal)
    print(" ")
    sleep(10)