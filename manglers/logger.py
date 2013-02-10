from scapy.all import *
import logging

class ScapyLogger:
	def mangle(self, packet):
		ip = IP(packet.get_data())
		logging.info(ip.summary())

