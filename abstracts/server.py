import socket
import thread
import logging

class TcpServer:
	def __init__(self, host, port, connections = 5):
		self.port = port
		self.host = host
		self.connections = connections
	
	def start(self):
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		logging.debug('Starting %s...' % self)
		serverSocket.bind((self.host, self.port))
		serverSocket.listen(self.connections)
		while 1:
			clientSocket, address = serverSocket.accept()
			thread.start_new_thread(self.process, (clientSocket, address))

	def process(self, clientSocket, address):
		raise NotImplementedError('This method has to be implemented in the inheriting class')
		
