# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
#  
#
# Example 1:
#
#
# Input: 1
# Output: "1"
#
#
# Example 2:
#
#
# Input: 4
# Output: "1211"
#


class Solution:
    def countAndSay(self, n: int) -> str:  # return a string
        # the sequence if given as in question
        if n==1:
            return str(1)
        'if n==2:'
        'return str(11)'
        a = list(self.countAndSay(n-1))
        res = []
        count = 1
        for i in range(len(a)-1):        # range(0) is [], when len(a)=1, will not enter for loop.
            if a[i]!=a[i+1]:
                res.append(str(count))
                res.append(a[i])
                count = 1
            else:
                count += 1
        res.append(str(count))
        res.append(a[-1])
        return "".join(res)
