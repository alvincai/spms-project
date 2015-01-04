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
	#sniff(iface="wave0", prn=lambda x: x.show())

	#sniff(iface="wave0", prn=lambda x: sendp(IP(src = IP_SRC, dst = IP_DST)/UDP(sport=1111, dport=UDP_DPORT)/"Hello!", iface="eth0"))
	#sniff(iface="wave0", prn=lambda x: sendp(Ether(dst="00:10:f3:3c:29:97", src="00:10:f3:3c:29:94", type=0x8946)/IP(src="10.11.11.15", dst ="10.11.11.34")/TCP(sport=1111, dport=5005), iface="eth0"))
