# Problem: Second Minimum Node In a Binary Tree
# Difficulty: Easy
# URL: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# Runtime: 0 ms
# Memory: 12.6 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        self.result = -1
        min_val = root.val
        def dfs(node):
            if not node:
                return
            if node.val > min_val:
                if self.result == -1 or node.val < self.result:
                    self.result = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.result