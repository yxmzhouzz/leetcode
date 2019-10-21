# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        for i, v in enumerate(nums):
            needed=target-v
            if needed in nums_map:
                return [nums_map[needed], i]   
                #in the map key is nums, value is index, return previous nums_map[needed] and current index i
            nums_map[v]=i  # if not in map, add [v, i] into map
        return [-1,-1]       
            
