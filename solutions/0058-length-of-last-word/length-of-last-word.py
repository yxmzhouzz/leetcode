# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
#
# Input: "Hello World"
# Output: 5
#
#
#  
#


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # if the last word not exist means no letters in the string
        if not s:
            return 0
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i]!=' ':
                count += 1
            if s[i]==' ' and count > 0:
                break
        return count
