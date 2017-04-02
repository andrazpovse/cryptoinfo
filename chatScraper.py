import dryscrape
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
session.visit("https://poloniex.com/exchange")
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
worthlessWords = ['the', 'i', 'and', 'is']

#is the word worthless....if it is, the functon will return True, else False
def isTheWordWorthless(word, worthlessWords):
	for i in worthlessWords:
		if (i == word):
			return True
	return False
#ce je IF stavek true tuple obrdzimo, ce je false, ga odstranimo
eliminatedWords = [i for i in wordAndCtr if(isTheWordWorthless(i[0], worthlessWords) == False)]

print eliminatedWords


