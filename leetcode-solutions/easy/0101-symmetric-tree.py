# Problem: Symmetric Tree
# Difficulty: Easy
# URL: https://leetcode.com/problems/symmetric-tree/
# Runtime: 5 ms
# Memory: 12.6 MB

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and 
                    isMirror(left.left, right.right) and 
                    isMirror(left.right, right.left))
        return isMirror(root.left, root.right) if root else True