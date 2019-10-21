# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
#
#
# Input: 16
# Output: true
#
#
#
# Example 2:
#
#
# Input: 14
# Output: false
#
#
#


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #return (int(num**0.5))**2 == num
        
        # newton's method f(x)=x**2-num
        # x_n+1 = xn-f(xn)/f'(xn)
        x = num
        while x**2 > num:
            x = (x+num/x)//2
        return x**2 == num
