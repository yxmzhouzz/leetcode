# -*- coding:utf-8 -*-


# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        res = ListNode(0)
        res.next = head
        temp = res
        
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            elif temp.next.val != val:      # need to use elif, only if will continue above if since temp.next is updated
                temp = temp.next        # temp 右移一格
        return res.next
        
