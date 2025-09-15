from converting import *
from math import ceil


class Network:
    def __init__(self, ip, cidr):
        self.ip = ip
        self.cidr = cidr

    def getSubnet(self):
        # Asking the user for the Classless Inter-Domain Routing value
        # It should be pure positive integer
        # Subnet mask as 1 or 0 digits
        mask = ['', '', '', '']

        # Filling mask with ones (network ID)
        for digit in range(self.cidr):
            if len(mask[0]) < 8:
                mask[0] += '1'
            elif len(mask[1]) < 8:
                mask[1] += '1'
            elif len(mask[2]) < 8:
                mask[2] += '1'
            elif len(mask[3]) < 8:
                mask[3] += '1'
        # Filling mask with zeros (host ID)
        for block in range(4):
            # While the block isn't full 8 bits, full the rest with zeros
            while len(mask[block]) < 8:
                mask[block] += '0'

        subnet_mask = ''
        for i in range(4):
            if i <= 2:
                subnet_mask += str(toDecimal(mask[i])) + '.'
            else:
                subnet_mask += str(toDecimal(mask[i]))
        # The result is string
        return subnet_mask

    def getNetworkIP(self):
        # We need subnet mask and ip then calculate the result of AND operation
        subnet = self.getSubnet()
        ip = self.ip
        # Convert ip and subnet mask to list of bytes
        ip_list = ip.split('.')
        mask_list = subnet.split('.')


        # Convert those lists to binary for AND operation
        ip_binary = []
        mask_binary = []
        for binary in ip_list:
            ip_binary.append(toBinary(int(binary)))
        for binary in mask_list:
            mask_binary.append(toBinary(int(binary)))


        # Now we need to perform the AND operation (complicated at my 1st attempt tbh)
        NetworkIP = ['','','','']

        for byte in range(4):
            for bit in range(8):
                NetworkIP[byte] += str(int(ip_binary[byte][bit]) and int(mask_binary[byte][bit]))

        NetworkAddress = []
        for byte in NetworkIP:
            NetworkAddress.append(str(toDecimal(byte)))

        # Convert to string
        Network = ".".join(NetworkAddress)
        return Network



host1 = Network('192.168.1.1', 24)
sub = host1.getSubnet()
netID = host1.getNetworkIP()
print(netID,sub)
