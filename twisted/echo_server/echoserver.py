#!/usr/bin/env python

from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
	def dataReceived(self, data):
		print "Data received: " + data
		print "Echoing data received back to client."
		self.transport.write(data)

class EchoFactory(protocol.Factory):
	def buildProtocol(self, addr):
		print "Building new Echo protocol."
		return Echo()

reactor.listenTCP(8000, EchoFactory())
reactor.run()
