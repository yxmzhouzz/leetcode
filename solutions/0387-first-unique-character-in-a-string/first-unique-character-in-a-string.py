# -*- coding:utf-8 -*-


#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return the first char which only shows once
        
        """
        # time limit
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1
        """
        
        """
        # use dictionary
        d = collections.Counter(s)
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1
        """
        
        # it's faster to check 26 different letters the loop the whole str
        letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
        indices = [s.index(x) for x in letters if s.count(x)==1]
        return min(indices) if indices else -1
        
