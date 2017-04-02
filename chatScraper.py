import dryscrape
import time
from collections import Counter
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser

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

stayAndWait = 20#how long to stay on the site...the longer, the more messages
for i in range(1,stayAndWait):
	print str(i)+"/"+str(stayAndWait)+" seconds passed"
	time.sleep(1)

response = session.body()

soup = BeautifulSoup(response, "lxml")
result = soup.find(id="trollbox") #trollboxtable messages

text = str(result) #turn beautifulsoup into a string
messages = strip_tags(text) #strip only messages from html

#count occurencies
messages = messages.split()
wordAndCtr = Counter(messages).most_common() #we get words and counter, occurencies of the word
#we get a list of tuples, ("word", times)
#must eliminate worthless words like "the", "and", ...
worthlessWords = ['will','or','that','for','the', 'i', 'and', 'is', 'in', 'on', 'you', 'a', 'your', 'it', 'this', 'my', 'to']

#is the word worthless....if it is, the functon will return True, else False
def isTheWordWorthless(word, worthlessWords):
	for i in worthlessWords:
		if (i == word):
			return True
	return False
#ce je IF stavek true tuple obrdzimo, ce je false, ga odstranimo
eliminatedWords = [i for i in wordAndCtr if(isTheWordWorthless(i[0], worthlessWords) == False)]

print eliminatedWords


