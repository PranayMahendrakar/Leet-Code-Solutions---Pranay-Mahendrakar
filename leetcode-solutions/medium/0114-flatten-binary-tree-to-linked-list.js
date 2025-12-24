# Problem: Flatten Binary Tree to Linked List
# Difficulty: Medium
# URL: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Runtime: 0 ms
# Memory: 55.2 MB

/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    let curr = root;
    
    while (curr) {
        if (curr.left) {
            // Find rightmost node in left subtree
            let prev = curr.left;
            while (prev.right) {
                prev = prev.right;
            }
            
            // Connect rightmost to current's right subtree
            prev.right = curr.right;
            
            // Move left subtree to right
            curr.right = curr.left;
            curr.left = null;
        }
        
        curr = curr.right;
    }
};