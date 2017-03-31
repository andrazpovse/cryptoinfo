import urllib, json


#Coinmarketcap limit API to 10 GET requests per 1 minute


#FUNCTIONS OMMITED BECAUSE THEY WOULD GENERATE TOO MUCH API REQUESTS


#gives you first 100 coins...coin one is at index [0] and so on to [99]
#dont know how they are sorted yet
def getFirst100CoinsData():
    response = urllib.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=100")
    data = json.loads(response.read())
    return data

#get price of coin.
#data....JSON object with coins
#coinName....name of the coin (e.g. Bitcoin, Monero, Steem, LBRY Credits)
#coinName also works with symbols (e.g. BTC, ICN, ETH)
def getPriceOfCoin(data, coinName):
    for i in range(0, len(data)):
        if(data[i]['name'] == coinName) or (data[i]['symbol'] == coinName):
            return data[i]['name'] + '  $'+data[i]['price_usd']



#not needed, since we pull first 100 coins...
#API get for first 100 coins
data = getFirst100CoinsData()

#Put the coins you want information on in a list
listOfCoins = ['ICN', 'LBC', 'Steem']

#goes through list, displays price of coins in the list
for i in listOfCoins:
	print getPriceOfCoin(data, i)




