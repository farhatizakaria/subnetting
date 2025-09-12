from converting import *

class Network:
    def __init__(self,ip,cidr) -> None:
        self.ip = ip
        self.cidr = cidr

    def getSubnet(self):
        # Asking the user for the Classless Inter-Domain Routing value
        # It should be pure positive integer
        # Subnet mask as 1 or 0 digits
        mask = ['','','','']

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
            if i <=2:
                subnet_mask += str(toDecimal(mask[i])) + '.'
            else:
                subnet_mask += str(toDecimal(mask[i]))

        print(subnet_mask)

net1 = Network('192.168.1.1',24)
net1.getSubnet()
