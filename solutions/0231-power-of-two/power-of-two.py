# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
#
# Input: 1
# Output: true 
# Explanation: 20 = 1
#
#
# Example 2:
#
#
# Input: 16
# Output: true
# Explanation: 24 = 16
#
# Example 3:
#
#
# Input: 218
# Output: false
#


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        #return sum(int(x) for x in bin(n)[2:])==1
        if n <= 0:
            return False
        if n > 0:
            return n&(n-1) == 0
            # if n is power of 2 will be 100000
            # and n-1 will be 011111, all bits are different
        
