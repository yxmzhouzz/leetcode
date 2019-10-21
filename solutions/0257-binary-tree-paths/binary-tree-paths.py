# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        #use deque BFS
        if not root:
            return []
        
        queue = collections.deque([(root, "")])
        res = []
        
        while queue:
            nd, path = queue.popleft()
            if not nd.left and not nd.right:
                res.append(path + str(nd.val))
            if nd.left:
                queue.append([nd.left, path + str(nd.val) + "->"])
            if nd.right:
                queue.append([nd.right, path + str(nd.val) + "->"])
        return res
                
        
        
