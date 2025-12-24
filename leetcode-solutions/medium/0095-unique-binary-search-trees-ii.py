# Problem: Unique Binary Search Trees II
# Difficulty: Medium
# URL: https://leetcode.com/problems/unique-binary-search-trees-ii/
# Runtime: 0 ms
# Memory: 18.9 MB

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        
        def generate(start, end):
            if start > end:
                return [None]
            
            trees = []
            for root_val in range(start, end + 1):
                left_trees = generate(start, root_val - 1)
                right_trees = generate(root_val + 1, end)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)
            
            return trees
        
        return generate(1, n)