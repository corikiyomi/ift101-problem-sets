# Network Device Inventory
    # lists, tuples, sets, dictionaries
    
# Goal: manage IP addresses, MAC addresses, device types in network

#List containing IP addresses as strings
device_ip = ['192.168.1.1']
devices = ['router', 'switch', 'server', 'workstation', 'printer', 'mobile device']

get_last = device_ip[0].split('.')

new_last = int(get_last[3])

print('List of IP Addresses:\n')
#Print each device's IP address on a new line
for ip in range(len(devices)):
    ip = get_last[:3]
    ip.append(str(new_last))
    new_ip = '.'.join(ip)
    device_ip.append(new_ip)
    print(f'{new_ip}\n')
    new_last += 1

device_ip = sorted(list(set(device_ip)))

#MAC addresses
device_mac = ('00:14:22:01:23:45')
list_device_mac = []
get_mac_last = device_mac.split(':')

new_mac_last = int(get_mac_last[5])

print('Tuple of MAC Addresses:\n')
#Print each MAC address on a new line
for mac in range(len(devices)):
    mac = get_mac_last[:5]
    mac.append(str(new_mac_last))
    new_mac_address = ':'.join(mac)
    list_device_mac.append(new_mac_address)
    device_mac = tuple(list_device_mac)
    print(f'{new_mac_address}\n')
    new_mac_last += 1
    
#Create set device_type
print('Set of Device Types:')
device_type = set(devices)
for device in device_type:
    print(f'{device} \n')
    
#Create a list named device_types
device_types = devices

#Create nested dictionary named network_inventory
    # keys = IP addresses
print('Network Inventory:')
network_inventory = {}
i_dict_values = list(zip(device_mac, device_types))
i = 0


while i < len(device_ip)-1:
    for ip in device_ip:
        network_inventory.setdefault(ip, i_dict_values[i])
        print(f'IP: {ip}, MAC: {i_dict_values[i][0]}, Type: {i_dict_values[i][1]}')
        i += 1

            
            
        