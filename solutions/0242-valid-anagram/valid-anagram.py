# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        # exceed time limit
        dic = {}
        for v in s:
            dic[v] = s.count(v)
        
        if len(set(s))!= len(set(t)):
            return False
        
        for val in t:
            if val not in dic:
                return False
            if dic[val] != t.count(val):
                return False
        return True
        """
        #string don't have sort() attribute
        #return sorted(s)==sorted(t)
        
        return collections.Counter(s) == collections.Counter(t)
