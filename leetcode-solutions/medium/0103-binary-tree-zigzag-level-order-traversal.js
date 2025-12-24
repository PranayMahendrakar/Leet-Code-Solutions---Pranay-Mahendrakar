# Problem: Binary Tree Zigzag Level Order Traversal
# Difficulty: Medium
# URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Runtime: 0 ms
# Memory: 54.6 MB

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
    if (!root) return [];
    
    const result = [];
    const queue = [root];
    let leftToRight = true;
    
    while (queue.length > 0) {
        const levelSize = queue.length;
        const level = [];
        
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift();
            
            if (leftToRight) {
                level.push(node.val);
            } else {
                level.unshift(node.val);
            }
            
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        
        result.push(level);
        leftToRight = !leftToRight;
    }
    
    return result;
};