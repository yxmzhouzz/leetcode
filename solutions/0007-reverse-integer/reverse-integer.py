# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#


class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        str_num = str(abs(x))
        re_str = str_num[::-1]
        sol = int(re_str)   # if "001", convert to int will be 1
        
        if is_neg:
            sol = -1*sol
        
        if sol < -2**31 or sol > (2**31-1):
            return 0
        else:
            return sol
