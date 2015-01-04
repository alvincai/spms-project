# /usr/bin/python

from scapy.all import *
import sys
import socket
from udpSender import *

if __name__ == "__main__":
	IP_DST = "10.8.0.18"	# Make this user input
	UDP_DPORT = 5005
	MESSAGE = "Hello!"

	sender = udpSender()
	sender.init(IP_DST, UDP_DPORT, MESSAGE)
	sniff(iface="wave0", prn=lambda x: sender.sendCustomPacket())

