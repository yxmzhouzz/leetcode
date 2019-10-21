# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.countpath = 0  # global variable
        
        self.dfs(root, sum)
        
        return self.countpath
    
    # dfs 用于把每个node走一遍，以每个node为起始点
    def dfs(self, root, target):
        if not root:
            return
        self.test(root, target)
        self.dfs(root.left, target)
        self.dfs(root.right, target)
    
    # test 用于从给定的起点找有没有path符合条件
    def test(self, root, target):
        if not root:
            return
        
        if root.val == target:
            self.countpath += 1
        
        self.test(root.left, target-root.val)
        self.test(root.right, target-root.val)
