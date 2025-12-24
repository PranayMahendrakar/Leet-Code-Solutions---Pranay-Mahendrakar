# Problem: N-ary Tree Postorder Traversal
# Difficulty: Easy
# URL: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# Runtime: 36 ms
# Memory: 15.7 MB

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children)
        return result[::-1]