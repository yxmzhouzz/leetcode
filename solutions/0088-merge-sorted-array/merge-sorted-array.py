# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
#
# 	The number of elements initialized in nums1 and nums2 are m and n respectively.
# 	You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
#
#
# Example:
#
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#


from collections import deque
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        by myself, not seccessful
        i=0
        j=0
        nums1 = nums1[:m]
        while i<m+n and j<n:
            # insert in list l.insert(index,ele)
            if nums1[i]>nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
            i += 1
        if nums2:
            nums1.extend(nums2[j:])
        """
        """
        # O((m+n)log(m+n))
        nums1[:]=nums1[:m]+nums2
        nums1.sort()
        """
        
        # O(m+n)
        if not nums1 or not nums2:
            return
        dq1 = deque(nums1[:m])
        dq2 = deque(nums2[:n])
        nums1[:]=[]
        while dq1 and dq2:
            if dq1[0]<=dq2[0]:
                nums1.append(dq1.popleft())
                  #deque.popleft() is faster than list.pop(0): O(1) VS O(n)
            else:
                nums1.append(dq2.popleft())
        nums1 += dq1 or dq2       
