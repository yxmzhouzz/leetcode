# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example, given a 3-ary tree:
#
#  
#
#
#
#  
#
# We should return its level order traversal:
#
#
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#
#
#  
#
# Note:
#
#
# 	The depth of the tree is at most 1000.
# 	The total number of nodes is at most 5000.
#
#


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# an m-ary tree is a rooted tree in which each node has no more than m children
# BFS, leave n position for each child

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []   #this if has same effect as while any(queue)
        
        queue = [root]
        res = []
        
        while queue:    # [None] is true, will enter into this while
                        # so we need if to check if root None or use any(queue)
            res.append([node.val for node in queue])
            # update queue
            queue = [child for node in queue for child in node.children if child]
        
        return res
