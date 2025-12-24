# Problem: Construct Binary Tree from Preorder and Inorder Traversal
# Difficulty: Medium
# URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Runtime: 7 ms
# Memory: 17 MB

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def build(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)