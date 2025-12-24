# Problem: Minimum Depth of Binary Tree
# Difficulty: Easy
# URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Runtime: 158 ms
# Memory: 95.1 MB

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))