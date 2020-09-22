#! python3

import ipaddress

try:
    ipchk = ipaddress.ip_address(input("Apply an IP address: "))
except:
    ipchk = "Invalid IP address format entered"

# a provided string will test true
if ipchk == ipaddress.ip_address("192.168.70.1"):
    print(f"Looks like the IP address of the Gateway was set: {ipchk}. This is not recommended.")
elif type(ipchk) == str: # if ipchk creation threw an error
   print(ipchk)
elif ipchk:
   print(f"Looks like an IP Adress was set: {ipchk}")
else:    # if data is NOT provided
   print("You did not provide input.") # indented under else