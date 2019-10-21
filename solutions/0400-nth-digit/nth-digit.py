# -*- coding:utf-8 -*-


# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
#
#
#
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
#
#


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        n -= 1
        
        for i in range(1,12):
            if n < i*9*10**(i-1):
                return int(str(10**(i-1) + n//i)[n%i])
            n = n-i*9*10**(i-1)  # i*9*10**(i-1) 为每一个group内的左右digits数
            
        
