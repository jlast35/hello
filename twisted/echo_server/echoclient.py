#!/usr/bin/env python

from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):

	def connectionMade(self):
		print "Connected to server."
		print "Sending message to server."
		self.transport.write("Hello, world!")

	def dataReceived(self, data):
		print "Data received from server."
		print "Server said:", data
		self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):

	def buildProtocol(self, addr):
		print "Building new EchoClient protocol."
		return EchoClient()

	def clientConnectionFailed(self, connector, reason):
		print "Connection failed."
		reactor.stop()

	def clientConnectionLost(self, connector, reason):
		print "Connection lost."
		reactor.stop()

print "Connecting to server."
reactor.connectTCP("localhost", 8000, EchoFactory())
reactor.run()
