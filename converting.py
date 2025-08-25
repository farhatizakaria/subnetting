# This script made only for converting binary-decimal purposes
def toDecimal(binary):
    if len(binary) == 8:
        total = 0
        k = 7
        for i in range(0,8):
            prod = int(binary[i]) * 2 ** k
            total += prod
            k = k - 1
        print(total)
    else:
        print('Make sure the given binary should be in 8-digits form')

def toBinary(decimal):
    decimal_result = ''
    while True:
        q = decimal // 2
        r = decimal % 2
        # We care with the rest of given decimal with 2
        decimal_result += str(r)
        # Exchange to divise the new given result and keep the loop going
        decimal = q
        # If the result is 0 break the loop
        if q == 0:
            break
    # We need to inverse the result's order
    result = decimal_result[::-1]
    missing_zeros = 8 - len(result)
    result = missing_zeros * '0' + result
    print(result)

#toDecimal('01100100') # Done
toBinary(700) # Done
