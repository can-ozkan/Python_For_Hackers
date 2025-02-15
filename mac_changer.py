"""
author: Can Ozkan
make sure to execute this program as root
How to change the mac address manually 

ifconfig eth0 down
ifconfig eth0 hw ether 00:11:22:33:44:55
ifconfig eth0 up

"""

import subprocess
import optparse
import re

def getUserInput():
    parseObject = optparse.OptionParser()
    parseObject.add_option("-i", "--interface", dest="interface", help="interface to be changed")
    parseObject.add_option("-m", "--mac", dest="newMacAddress", help="new MAC address")

    #print(parseObject.parse_args()) This returns a tuple
    return parseObject.parse_args()


def changeMacAddress(userInterface, newMacAddress):
    subprocess.run(["ifconfig", userInterface, "down"])
    subprocess.run(["ifconfig", userInterface, "hw", "ether", newMacAddress])
    subprocess.run(["ifconfig", userInterface, "up"])

def controlNewMac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    #print(ifconfig)
    newMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if newMac:
        return newMac.group(0)
    else:
        return None

print("Welcome to the MAC changer program")
print("This program should be leveraged to change the MAC address")

(userInput, arguments) = getUserInput()
changeMacAddress(userInput.interface, userInput.newMacAddress)
finalMac = str(controlNewMac(userInput.interface))

if finalMac == userInput.newMacAddress:
    print("Your MAC address has been successfully changed")
else:
    print("An error occurred")

