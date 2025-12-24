# Problem: Binary Tree Inorder Traversal
# Difficulty: Easy
# URL: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Runtime: 0 ms
# Memory: 12.3 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        inorder(root)
        return result