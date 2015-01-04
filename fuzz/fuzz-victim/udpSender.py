# /usr/bin/python

from scapy.all import *
import sys
import socket

class udpSender:
	def init(self, IP_DST, UDP_DPORT, MESSAGE):
		self.IP_DST = IP_DST
		self.UDP_DPORT = UDP_DPORT
		self.MESSAGE = MESSAGE
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def sendCustomPacket(self):
		self.sock.sendto(self.MESSAGE, (self.IP_DST, self.UDP_DPORT))

