import urllib, json

#Coinmarketcap limit API to 10 GET requests per 1 minute




#API GET gives you first 100 coins...coin one is at index [0] and so on to [99]
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
#percent_change_1h
def getPercentChange24h(data, coinName):
    for i in range(0, len(data)):
    	if(data[i]['name'] == coinName) or (data[i]['symbol'] == coinName):
            return data[i]['name']+data[i]['percent_change_1h']+' %'

#gets you some info on the coin...price, 24h change, 1h change
def getSomeInfo(data, coinName):
	for i in range(0, len(data)):
		if(data[i]['name'] == coinName) or (data[i]['symbol'] == coinName):
			return data[i]['name'] + '\nPrice: $' + data[i]['price_usd'] + '\n1h change: '+ data[i]['percent_change_1h']+'%\n24h change: ' + data[i]['percent_change_24h'] + '%\n'


data = getFirst100CoinsData()

#Put the coins you want information on in a list
listOfCoins = ['ICN', 'LBC', 'Steem']



# TO DO
""" 
timer function, so the data would print itself every 5 minutes
GUI
Connect with database, to display charts, maybe predict
"""


#goes through list, displays price of coins in the list
for i in listOfCoins:
	print getSomeInfo(data, i)




