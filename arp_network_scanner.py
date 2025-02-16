"""
author: Can Ozkan

This program performs an ARP scan to th given network range.
Therefore, users can get IP address and MAC address pairs.

"""

import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-r", "--range", dest="ip_address_range", help="IP address range")

    (user_input, arguments) = parse_object.parse_args()

    if not user_input.ip_address_range:
        print("Invalid IP address range")
        exit()
    
    return user_input.ip_address_range

def arp_scan(ip_range):
    # Create ARP request
    arp_request = scapy.ARP(pdst=ip_range)
    
    # Create Ethernet frame (broadcast)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Combine both into a single packet
    packet = broadcast / arp_request
    
    # Send and receive packets
    answered, unanswered = scapy.srp(packet, timeout=3, verbose=False)

    print("IP Address\t\tMAC Address")
    print("-" * 40)
    
    for sent, received in answered:
        print(f"{received.psrc}\t\t{received.hwsrc}")

# Replace with your correct subnet
user_ip_address = get_user_input()
arp_scan(user_ip_address)
