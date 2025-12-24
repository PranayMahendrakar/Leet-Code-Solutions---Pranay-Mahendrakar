# Problem: N-ary Tree Preorder Traversal
# Difficulty: Easy
# URL: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# Runtime: 48 ms
# Memory: 18.7 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(reversed(node.children))
        return result