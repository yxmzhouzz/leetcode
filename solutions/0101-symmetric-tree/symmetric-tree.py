# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#  
#
# But the following [1,2,2,null,3,null,3] is not:
#
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#  
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(root1, root2):
            # need the below 2 if in the body of isSym to judge recursively till the end stopping condition
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return root1.val == root2.val and isSym(root1.left, root2.right) and isSym(root1.right, root2.left)
        
        if not root:
            return True
        
        return isSym(root.left, root.right)
    
        
            
