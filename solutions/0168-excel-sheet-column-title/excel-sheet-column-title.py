# -*- coding:utf-8 -*-


# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
#
#
# Example 1:
#
#
# Input: 1
# Output: "A"
#
#
# Example 2:
#
#
# Input: 28
# Output: "AB"
#
#
# Example 3:
#
#
# Input: 701
# Output: "ZY"
#


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        
        res = []
        while n > 0:
            res.append(letters[(n-1) % 26])
            n = (n-1) // 26
        
        titles = "".join(res)
        return titles[::-1]
        
            
