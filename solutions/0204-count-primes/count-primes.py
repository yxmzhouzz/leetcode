# -*- coding:utf-8 -*-


# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 2:
            return 0
        isprime = [1]*n # from 0 to n-1
        for i in range(2, int(n**0.5)+1):
            
            #for j in range(i*i, n, i):
            #    isprime[j] = 0
            
            isprime[i*i:n:i]=[0]*((n-1-i*i)//i+1)
            
            
        return sum(isprime)-2
    
    """
# Sieve of Eratosthenes
Input: an integer n > 1
 
Let A be an array of Boolean values, indexed by integers 2 to n,
initially all set to true.
 
for i = 2, 3, 4, ..., not exceeding \sqrt {n}
  if A[i] is true:
    for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n :  因为比i小的倍数已经检查过，所以从i^2开始
      A[j] := false
 
Output: all i such that A[i] is true.
"""
