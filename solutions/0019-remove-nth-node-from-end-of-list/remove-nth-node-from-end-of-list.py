# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
#
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        list_len=0
        temp=head
        while temp.next:
            list_len+=1
            temp=temp.next
        list_len+=1
        
        count=0
        dd=res=ListNode(0)
        while count<list_len-n:
            res.next=head
            head=head.next
            res=res.next
            count+=1
            
        head=head.next
        res.next=head
        
        return dd.next
