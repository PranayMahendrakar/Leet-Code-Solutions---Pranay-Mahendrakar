# Problem: Binary Tree Level Order Traversal II
# Difficulty: Medium
# URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Runtime: 0 ms
# Memory: 57.8 MB

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrderBottom = function(root) {
    if (!root) return [];
    
    const result = [];
    const queue = [root];
    
    while (queue.length > 0) {
        const levelSize = queue.length;
        const level = [];
        
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift();
            level.push(node.val);
            
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        
        result.unshift(level);  // Add to front instead of end
    }
    
    return result;
};