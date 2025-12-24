# Problem: Sum of Left Leaves
# Difficulty: Easy
# URL: https://leetcode.com/problems/sum-of-left-leaves/
# Runtime: 0 ms
# Memory: 13.2 MB

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        total = 0
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        return total + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)