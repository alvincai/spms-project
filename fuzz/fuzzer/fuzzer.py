#! /usr/bin/python
from scapy.all import *
import sys
import pcap
import socket
import time

if __name__ == "__main__":

	'''This setup assumes that the fuzzer has the following characteristics
	IP Address of ethernet card is 10.8.0.18
	MAC address of 802.11p card is 30:14:4a:d9:f8:7a
	'''
	UDP_IP = "10.8.0.18"
	UDP_PORT = 5005
	wave0_MAC = "30:14:4a:d9:f8:7a"
	
	'''The setup assumes that the victim has the following characteristics
	MAC address of 802.11p card is 30:14:4a:d9:f8:7a
	'''
	wave0_MAC_victim = "30:14:4a:d9:f8:8a"

	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock.bind((UDP_IP, UDP_PORT))
	sock.settimeout(5.0)	# Set the timeout for a response from the fuzzed client to 5 seconds

	fuzzInputs = list()	# Inputs which cause a crash

	for i in range(65536):
		sendp(Ether(dst = wave0_MAC_victim, src = wave0_MAC, type=i), iface="wave0")
		try:
			data, addr = sock.recvfrom(1024)
			print "received message:", data
		except:
			# Try sending a known packet. Maybe the victim did not receive or parse the previous packet
			sendp(Ether(dst = wave0_MAC_victim, src = wave0_MAC, type=0x8946), iface="wave0")
			try:
				data, addr = sock.recvfrom(1024)
				print "receieved message:", data
			except:
				print "timed out, failed at %d"%i
				fuzzInputs.append(i)
	
	logfile = open('log.txt', 'w')
	for item in fuzzInputs:
		print>>logfile, item
