# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
#
# Input: "hello"
# Output: "holle"
#
#
#
# Example 2:
#
#
# Input: "leetcode"
# Output: "leotcede"
#
#
# Note:
# The vowels does not include the letter "y".
#
#  
#


class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return ""
        
        vowels = "aeiou"
        ss = list(s)
        l = 0
        r = len(s)-1
        
        while l < r:
            while l < len(s) and s[l].lower() not in vowels:  # !!!capital letter and infinite while loop make l out of range
                l += 1
            while r > 0 and s[r].lower() not in vowels:
                r -= 1
            if l<r:
                ss[l], ss[r] = ss[r], ss[l]
                l += 1
                r -= 1
        return "".join(ss)
                
            
