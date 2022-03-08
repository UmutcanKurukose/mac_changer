import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="intarface",help="Entery your interface")
parse_object.add_option("-m","--mac_address",dest="mac_address", help="Entry your want it mac address")

(user_inputs,argument) = parse_object.parse_args()

user_interface = user_inputs.interface
user_mac_adress= user_inputs.mac_adress

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_adress])
subprocess.call(["ifcongif",user_interface,"up"])
