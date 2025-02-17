#pip3 install scapy_http
#in this program, the objective is to listen to http traffics
#this program can be combined with mitm attack.
#change the interface in the listen_packets function call
#you can use sslstrip and dns2proxy for https sites that do not support hsts

import scapy.all as scapy
from scapy_http import http

def listen_packets(interface):
    scapy.sniff(iface=interface, store=False, prn=analyze_packets)

    #prn is a callback function

def analyze_packets(packet):
    # packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            packet[scapy.Raw].load

listen_packets("eth0")
