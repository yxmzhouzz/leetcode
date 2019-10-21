# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
#
# Example: 
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
#


class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # sets has the elements of odd qty
        sets = set()
        for x in s:
            if x not in sets:
                sets.add(x)
            else:
                sets.remove(x)
        
        return len(s)-len(sets)+1 if sets else len(s) # can only choose one from odd sets
