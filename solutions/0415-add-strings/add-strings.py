# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # length too long, can't convert into integer do addition
        carry = 0  # 进位
        res = []
        l1 = list(num1)
        l2 = list(num2)
        while l1 or l2:
            n1 = int(l1.pop()) if l1 else 0
            n2 = int(l2.pop()) if l2 else 0
            temp = n1 + n2 + carry
            res.append(temp % 10)
            carry = temp // 10
        
        if carry: 
            res.append(carry)
        
        return "".join([str(i) for i in res])[::-1]
