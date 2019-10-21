# -*- coding:utf-8 -*-


# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
#
#
# Example 1:
#
#
# Input: "A"
# Output: 1
#
#
# Example 2:
#
#
# Input: "AB"
# Output: 28
#
#
# Example 3:
#
#
# Input: "ZY"
# Output: 701
#


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        
        nums = [letters.index(ele)+1 for ele in s]
        nums.reverse()
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]*26**i
        return sum1
        
        
