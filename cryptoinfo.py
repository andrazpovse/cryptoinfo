import urllib, json

#function getPriceOfCoin returns the price of the passed (with API url) coin in USD
def getPriceOfCoin(coinAPI):
   response = urllib.urlopen(coinAPI)
   data = json.loads(response.read())[0]
   priceUSD = "$" + data['price_usd'] 
   return priceUSD

#add coin API for coins you would like to get information on
iconomi = "https://api.coinmarketcap.com/v1/ticker/iconomi/"
lbry = "https://api.coinmarketcap.com/v1/ticker/library-credit/"
stratis = "https://api.coinmarketcap.com/v1/ticker/stratis/"


#calls for price in USD of a specific coin
priceUSD = getPriceOfCoin(lbry)


print priceUSD



