# This script made only for converting binary-decimal purposes
def toDecimal(binary):
    total = 0
    k = 7
    for i in range(0,8):
        prod = int(binary[i]) * 2 ** k
        total += prod
        k = k - 1
    print(total)

toDecimal('11001111')
