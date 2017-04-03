import urllib, json
from Tkinter import *
from multiprocessing import Process
import time, threading





global data #global variable that contains recent data from API call in JSON format
#when wanting to change data, use "global data" one line before the actual change
global listOfCoins #perhaps global will not be needed...just for now it is
#Put the coins you want information on in a list
#name of coin or symbol works aswell
listOfCoins = ['ICN', 'LBC', 'Steem']


#main is currently omitted....focus not on graphics design currenty
def main(): #run main loop GUI
	root = Tk()
	root.geometry("600x600")
	frame = Frame(root)

	frame.pack( side = BOTTOM )

	blackbutton = Button(frame, text="Change list", fg="Green")
	blackbutton.pack( side = BOTTOM)


	#def getData():
	#	getFirst100CoinsData() #changes global variable data
	#	root.after(1000*60*5, getData)  # get new data every 5 minutes from now on
	#getData() #first API call happens right after the program launches

	var = StringVar() #creates a label which will display coin info
	label = Label( root, textvariable=var )
	label.pack()
	def refreshCoinInfoScreen(): #updates the label text every 5 minutes, same as getData, when it refreshes
		var.set(informationOnList(listOfCoins))
		root.after(1000*60*5, refreshCoinInfoScreen)
	refreshCoinInfoScreen()



	root.mainloop()
#end of main



#Coinmarketcap limit API to 10 GET requests per 1 minute

#API GET gives you first 100 coins...coin one is at index [0] and so on to [99]
#dont know how they are sorted yet
def getFirst100CoinsData():
    print "getting some data on the coins"
    response = urllib.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=100")
    global data #uses the global variable and changes it to recent data
    data = json.loads(response.read())





#data....JSON object with coins
#coinName....name of the coin (e.g. Bitcoin, Monero, Steem, LBRY Credits)
#coinName also works with symbols (e.g. BTC, ICN, ETH)
#gets you some info on the coin...price, 24h change, 1h change
def getSomeInfo(data, coinName):
	for i in range(0, len(data)):
		if(data[i]['name'] == coinName) or (data[i]['symbol'] == coinName):
			return data[i]['name'] + '\nPrice: $' + data[i]['price_usd'] + '\n1h change: '+ data[i]['percent_change_1h']+'%\n24h change: ' + data[i]['percent_change_24h'] + '%\n\n'

#get info on a list of coins
def informationOnList(list):
	output=""
	for i in list:
		output += getSomeInfo(data, i)
	return output


def getData():
		getFirst100CoinsData() 
		print informationOnList(listOfCoins)
		time.sleep(60*5)
		getData()
		#threading.Timer(60*5, getData).start() #calls itself every 5 minutes
		
getData() 

#need to get coin names
def getCoinNames(data):
	out = ""
	for i in range(0, len(data)):
		out += "'"+data[i]['symbol']+"','"+data[i]['name']+"',"
	print out
#getFirst100CoinsData()


#getCoinNames(data)




#starts the main loop

# TO DO
""" 
timer function, so the data would print itself every 5 minutes
GUI
Connect with database, to display charts, maybe predict
"""

