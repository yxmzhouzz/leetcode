# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n2) EXCEED TIME LIMIT
        """
        if not nums:
            return 0
        max_sum = nums[0]
        for head in range(len(nums)):
            sum1 = nums[head]
            if sum1>max_sum:
                max_sum = sum1
            if head < len(nums)-1:
                for tail in range(head+1, len(nums)):
                    sum1 += nums[tail]
                    if sum1>max_sum:
                        max_sum = sum1
        return max_sum
        """
        
        # if sum += nums[current] < 0 , it will be no good for contrbuting largest sum array
        # so if find sum < 0 in the loop process, then jump to next
        if not nums:
            return 0
        max_sum = nums[0]
        s = nums[0]
        for tail in range(1, len(nums)):
            if s < 0:
                s = 0       # means restart sum from next tail as beginning
            s += nums[tail]
            if s > max_sum:
                max_sum = s 
        return max_sum
                
                
                
                
