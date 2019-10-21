# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# Example:
#
#
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.
#
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?


class Solution:
    def addDigits(self, num: int) -> int:
        """
        # while loop
        while len(str(num))!=1:
            num=sum([int(x) for x in str(num)])
        return num
        """
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
