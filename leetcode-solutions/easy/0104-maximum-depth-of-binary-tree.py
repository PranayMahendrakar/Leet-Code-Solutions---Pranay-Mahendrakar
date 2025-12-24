# Problem: Maximum Depth of Binary Tree
# Difficulty: Easy
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Runtime: 3 ms
# Memory: 15 MB

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))