import dryscrape
import time
from collections import Counter
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser


stayAndWait = 30#in seconds...how long to stay on the site...the longer, the more messages

#strips tags from HTMl
#http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()



session = dryscrape.Session()
print "establishing connection..."
session.visit("https://poloniex.com/exchange")

for i in range(1,stayAndWait):
	print str(i)+"/"+str(stayAndWait)+" seconds passed"
	time.sleep(1)

response = session.body()

soup = BeautifulSoup(response, "lxml")
result = soup.find(id="trollbox") #trollboxtable messages

text = str(result) #turn beautifulsoup into a string
messages = strip_tags(text) #strip only messages from html
#at this point, the messages are still in tact.....
#get sentence meaning here !!!-------------------------------------------------------------------------------------------------------------



#split messages by space
messages = messages.split()

#convert messages to lowercase
for i in range(0,len(messages)):
	messages[i] = messages[i].lower()



#we get words and counter, occurencies of the word
wordAndCtr = Counter(messages).most_common() 
#we get a list of tuples, ("word", times)
#must eliminate worthless words like "the", "and", ...
worthlessWords = ['just','what','will','or','that','for','the', 'i', 'and', 'is', 'in', 'on', 'you', 'a', 'your', 'it', 'this', 'my', 'to']


usefulCoinWords = ['BTC','Bitcoin','ETH','Ethereum','XRP','Ripple','DASH','Dash','LTC','Litecoin','XMR','Monero','ETC','Ethereum Classic','XEM','NEM','REP','Augur','MAID','MaidSafeCoin','GNT','Golem','ZEC','Zcash','DOGE','Dogecoin','USDT','Tether','DCR','Decred','ICN','Iconomi','PIVX','PIVX','STEEM','Steem','DGD','DigixDAO','WAVES','Waves','FCT','Factom','STRAT','Stratis','LSK','Lisk','BTS','BitShares','1ST','First Blood','XLM','Stellar Lumens','ROUND','Round','BCC','BitConnect','BCN','Bytecoin','SNGLS','SingularDTV','ARDR','Ardor','MLN','Melon','GAME','GameCredits','KMD','Komodo','PPC','Peercoin','NXT','Nxt','EMC','Emercoin','SC','Siacoin','NXS','Nexus','XCP','Counterparty','SJCX','Storjcoin X','NMC','Namecoin','SDC','ShadowCash','ANS','AntShares','CRBIT','Creditbit','BTCD','BitcoinDark','NLG','Gulden','BCY','Bitcrystals','XZC','ZCoin','GBYTE','Byteball','XAUR','Xaurum','SYS','SysCoin','IOC','I/O Coin','AMP','Synereo','YBC','YbCoin','BLK','BlackCoin','UBQ','Ubiq','RBY','Rubycoin','AGRS','Agoras Tokens','TIME','Chronobank','NAV','NAV Coin','POT','PotCoin','ARK','Ark','ION','ION','SLR','SolarCoin','NVC','Novacoin','GRC','GridCoin','CRW','Crown','NXC','Nexium','RADS','Radium','XPM','Primecoin','BAY','BitBay','VPN','VPNCoin','UNITY','SuperNET','PEPECASH','Pepe Cash','DGB','DigiByte','EXP','Expanse','XBC','Bitcoin Plus','OMNI','Omni','LBC','LBRY Credits','LMC','LoMoCoin','EDR','E-Dinar Coin','BELA','BelaCoin','CLAM','Clams','XBB','Boolberry','NAUT','NautilusCoin','AEON','Aeon','MUE','MonetaryUnit','MONA','MonaCoin','BURST','Burst','CURE','CureCoin','PASC','Pascal Coin','VTC','Vertcoin','ZCL','ZClassic','JINN','Jinn','ARC','ArcticCoin','VSL','vSlice','VIA','Viacoin','HEAT','HEAT','FAIR','FairCoin']



#get the trend based on text....integer
def downTrend(text):
	trendDOWN = ['down', 'drop', 'fall', 'sell']
	counter = 0;
	for i in text:
		for j in trendDOWN:
			if (i.lower() == j.lower()):
				counter+=1;

	return "Down trend is: " + str(counter)


#get the trend based on text....integer
def upTrend(text):
	trendUP = ['up', 'moon', 'rise', 'buy']
	counter = 0;
	for i in text:
		for j in trendUP:
			if (i.lower() == j.lower()):
				counter+=1;

	return "Up trend is: " + str(counter)


#is the word worthless....if it is, the functon will return True, else False
def isTheWordWorthless(word, worthlessWords):
	for i in worthlessWords:
		if (i.lower() == word.lower()):
			return True
	return False

#if the word is a coin, it will return True else false
def isTheWordACoin(word, coins):
	for i in coins:
		if (i.lower() == word.lower()): #comparison is in lower case
			return True
	return False
#ce je IF stavek true tuple obrdzimo, ce je false, ga odstranimo
coinMentions = [i for i in wordAndCtr if(isTheWordACoin(i[0], usefulCoinWords) == True)]
eliminatedWords = [i for i in wordAndCtr if(isTheWordWorthless(i[0], worthlessWords) == False)]

print coinMentions
print upTrend(messages)
print downTrend(messages)

