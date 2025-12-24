# Problem: Path Sum
# Difficulty: Easy
# URL: https://leetcode.com/problems/path-sum/
# Runtime: 0 ms
# Memory: 14.4 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        # If leaf node, check if current value equals remaining sum
        if not root.left and not root.right:
            return root.val == targetSum
        # Recursively check left and right subtrees
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)