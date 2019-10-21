#
# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
#
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
#
#
#
# Example 1:
#
# Input:
# 26
#
# Output:
# "1a"
#
#
#
# Example 2:
#
# Input:
# -1
#
# Output:
# "ffffffff"
#
#


class Solution:
    def toHex(self, num: int) -> str:
        # 16进制
        # n>>4*i do the multiplication first, then move right, same as divide 16 by i times
        
        return ''.join('0123456789abcdef'[(num>>4*i)&15] for i in range(8))[::-1].lstrip('0') or '0'
        
        # (num>>4*i)&15 : &15 返回所有小于等于15的值
        # num>>4*i相当于num//(4i), 只不过这里i从0开始，不能除
        # lstrip('0') or '0'去除前面所有0， 只剩一个0的话保留
