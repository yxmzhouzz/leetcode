# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
#
#
# Note:
#
# You may assume that the array does not change.
# There are many calls to sumRange function.
#
#


class NumArray:

    def __init__(self, nums: List[int]):
        self.ar = nums
        for i in range(1, len(nums)):
            self.ar[i] += self.ar[i-1]  # itertools.accumulate usage
        

    def sumRange(self, i: int, j: int) -> int:
        #return sum(self.ar[i:j+1])
        """
        #too slow
        sum = 0
        for x in range(i, j+1):
            sum += self.ar[x]
        return sum
        """
        return self.ar[j]-(self.ar[i-1] if i > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
