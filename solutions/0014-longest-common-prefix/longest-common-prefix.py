# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        min_len = min(len(strs[0]), len(strs[-1]))
        
        indx = min_len
        for i in range(min_len):
            if strs[0][i]!=strs[-1][i]:
                indx = i-1
                break
        
        if indx == -1:
            return ""
        return strs[0][0:indx+1]
