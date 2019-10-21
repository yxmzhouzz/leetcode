# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
#
#
# Example 2:
#
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false
#
#
# Example 3:
#
#
# Input:     1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# Output: false
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        # recursion method
        if not p and not q:     # p q are both none
            return True
        elif not p or not q:    # one of p, q is none
            return False
        # the first 2 if will be used in recursion cloing to end
        if p.val==q.val:        # p, q are both not none
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else: 
            return False
        """
        
        # traverse tree
        def traverse_to_list(tree, l):
            if tree:
                l.append(tree.val)
                traverse_to_list(tree.left, l)
                traverse_to_list(tree.right, l)
            else:
                l.append(0)
            return l
        return traverse_to_list(p, []) == traverse_to_list(q, [])
            
