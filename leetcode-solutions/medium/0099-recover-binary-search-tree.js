# Problem: Recover Binary Search Tree
# Difficulty: Medium
# URL: https://leetcode.com/problems/recover-binary-search-tree/
# Runtime: 3 ms
# Memory: 65.7 MB

/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var recoverTree = function(root) {
    let first = null, second = null, prev = null;
    
    const inorder = (node) => {
        if (!node) return;
        
        inorder(node.left);
        
        if (prev && prev.val > node.val) {
            if (!first) {
                first = prev;
            }
            second = node;
        }
        prev = node;
        
        inorder(node.right);
    };
    
    inorder(root);
    
    // Swap values
    const temp = first.val;
    first.val = second.val;
    second.val = temp;
};