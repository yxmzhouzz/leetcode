# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
#
# Example 1:
#
#
# Input: a = 1, b = 2
# Output: 3
#
#
#
# Example 2:
#
#
# Input: a = -2, b = 3
# Output: 1
#
#
#
#


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        l = [a, b]
        return sum(l)
        """
        
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        
        # two's complement
        m = 0xffffffff   # i is all 1 on 32 digits, a&i == a, a^i = i-a if a>0; -i-a if a<0
        
        while b!=0:
            a,  b = (a^b) & m, (a&b)<<1 & m
        return a if a<MAX else ~(a^m)
        
        
        
