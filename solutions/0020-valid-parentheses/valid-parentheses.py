# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# 	Open brackets must be closed by the same type of brackets.
# 	Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        pmap = {'(':')', '{':'}', '[':']'}
        stack = []
        for ele in s:
            if ele in pmap:
                stack.append(ele)
            elif len(stack)!=0 and pmap[stack[-1]]==ele:
                stack.pop()
            else:
                return False
            
        if not stack:
            return True
        else:
            return False
