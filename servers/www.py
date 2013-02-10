from abstracts.server import TcpServer

class WwwServer(TcpServer):
	def __init__(self, host = '', port = 80):
		TcpServer.__init__(self, host, port)

	def process(self, clientSocket, clientAddress):
		data = clientSocket.recv(1024)
		clientSocket.send('It works!')
		clientSocket.close()

	def __str__(self):
		return "Simple WWW Server @ %s:%s" % (self.host, self.port)
