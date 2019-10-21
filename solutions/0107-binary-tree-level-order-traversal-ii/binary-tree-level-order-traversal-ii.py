# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        if not root:
            return []
        s = [root]
        
        res = [[root.val]]
        while s:
            each_level = []
            each_level_value = []
            
            while s:
                top = s.pop(0)  # if pop() the rightmost will be popped out first
            
                if top.left:
                    each_level.append(top.left)
                    each_level_value.append(top.left.val)
                if top.right:
                    each_level.append(top.right)
                    each_level_value.append(top.right.val)
            s = each_level
            if each_level_value:
                res.append(each_level_value)
        
        rev_res = []
        while res:
            rev_res.append(res.pop())
        return rev_res
        """
        
        if not root:
            return []
        
        ans = []
        each_level = [root]
        while each_level:
            ans.insert(0, [i.val for i in each_level])   # insert from front
            each_level = [j for i in each_level for j in (i.left, i.right) if j]  # update each_level using next level
        return ans
