class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitMask = 0xffffffff
        
        while (b & bitMask) > 0 :
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        return (a & bitMask) if b > 0 else a