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
    sock.settimeout(5.0)        # Set the timeout for a response from the fuzzed client to 5 seconds

    fuzzInputs = list()	        # Inputs which cause a crash


    '''
    The code below fuzzes the FCfield, ID and SC fields.
    Amend accordingly for your own application
    '''
    for i in range(256):
        for j in range(65536):  # 0xffff (2 bytes) = 65535
            for k in range (65536):
                sendp(Dot11(addr1 = wave0_MAC_victim, addr2 = wave0_MAC, FCfield = i, ID = j, SC = k), iface="wave0")
        	try:
        	    data, addr = sock.recvfrom(1024)
        	    print "received message:", data
                except:
                    '''
                    Maybe the victim did not receive or parse the previous packet
                    Try sending a packet which is known to be accepted and the victim responds too
                    Amend the packet below accordingly
                    '''
                    sendp(Dot11(addr1 = wave0_MAC_victim, addr2 = wave0_MAC), iface="wave0")
        	    try:
        	        data, addr = sock.recvfrom(1024)
        		print "receieved message:", data
        		except:
        		    print "timed out, failed at %d"%i
        		    fuzzInputs.append(i)


    # Fuzzing is over. Save list of fuzzed inputs (which caused a crash) to disk (log.txt)
    logfile = open('log.txt', 'w')
    for item in fuzzInputs:
        print>>logfile, item
