import subprocess
import optparse
import re

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="Entery your interface")
    parse_object.add_option("-m","--mac_address",dest="mac_address", help="Entry your want it mac address")

    return parse_object.parse_args()

def change_mac_adress(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifcongif",user_interface,"up"])

def control_new_mac(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print ("MacChanger Started!")
(user_inputs,argument) = get_user_input()
change_mac_adress(user_inputs.interfaces,user_inputs.mac_address)
finalized_mac = control_new_mac(user_inputs.interfaces)

if finalized_mac == user_inputs.mac_address:
    print("success")
else:
    print("Error!!")