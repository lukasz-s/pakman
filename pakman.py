from core.settings import Settings
import thread, sys
import logging
import os
import nfqueue
import socket

def getSettings():
	if os.path.isfile('settings.yaml'):
		with open('settings.yaml') as f:
			return Settings(f)
	else:
		return Settings(__import__('settings'))

def startServers(settings):
   servers = settings.getServers()
   for server in servers:
      thread.start_new_thread(server.start, ())

def nfCallback(packet):
	for mangler in manglers:
		mangler.mangle(packet)

def startNfQueue(settings):
	queue = nfqueue.queue()
	queue.open()
	queue.bind(socket.AF_INET)
	queue.set_callback(nfCallback)
	queue.create_queue(0)
	queue.set_queue_maxlen(5000)
	try:
		queue.try_run()
	except KeyboardInterrupt:
		queue.unbind(socket.AF_INET)
		queue.close()

def main():
	settings = getSettings()
	global manglers
	manglers = settings.getManglers()
	startServers(settings)
	startNfQueue(settings)

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	main()
