# Asking the user for the Classless Inter-Domain Routing value
# It should be pure positive integer
cidr_user = int(input('Write your prefered CIDR value: '))
mask = ['','','','']
for digit in range(cidr_user+1):
    if len(mask[0]) < 8:
        mask[0] += '1'
    elif len(mask[1]) < 8:
        mask[1] += '1'
    elif len(mask[2]) < 8:
        mask[2] += '1'
    elif len(mask[3]) < 8:
        mask[3] += '1'
print(mask)
