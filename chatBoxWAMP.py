from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


def tamperMessage(message):
	print message.split()[0]



class MyComponent(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        print("session joined")
        
        def gotMessage(type, messageNumber, username, message, reputation):
        	tamperMessage(message)
        	
        # 1. subscribe to a topic so we receive events
        try:
        	yield self.subscribe(gotMessage,u'trollbox')
        	print "subscribed"
        except Exception as e:
            print("could not subscribe to topic:")

runner = ApplicationRunner(url=u"wss://api.poloniex.com", realm=u"realm1")
runner.run(MyComponent)