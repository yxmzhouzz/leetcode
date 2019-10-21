# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # recursion
        if not root:
            return 0  # can't be None
        
        """
        sum = 0
        
        each_line = collections.deque([root])
        
        while each_line:
            top = each_line.popleft()
            if top.left:
                each_line.append(top.left)
            if top.right:
                each_line.append(top.right)
        """
        
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
