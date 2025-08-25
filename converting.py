# This script made only for converting binary-decimal purposes
def toDecimal(binary:str) -> int:
    if len(binary) == 8:
        total = 0
        k = 7 # The loop will begin from 2⁷, so k=7 then decrement it through for loop
        for i in range(0,8):
            prod = int(binary[i]) * 2 ** k
            total += prod
            k = k - 1
        return total
    else:
        print('Make sure the given binary should be full byte form (8 bits)')

def toBinary(decimal:int) -> str:
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
    # Check missing zeros at the left, because we need results to be as full Byte form (8 bits)
    missing_zeros = 8 - len(result)
    result = missing_zeros * '0' + result
    return result

a = (toDecimal('00000100')) # Done
b = (toBinary(18)) # Done
print(a)
print(b)
