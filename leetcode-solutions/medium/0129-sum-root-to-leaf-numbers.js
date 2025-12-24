# Problem: Sum Root to Leaf Numbers
# Difficulty: Medium
# URL: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Runtime: 0 ms
# Memory: 52.3 MB

/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumNumbers = function(root) {
    const dfs = (node, num) => {
        if (!node) return 0;
        
        num = num * 10 + node.val;
        
        if (!node.left && !node.right) {
            return num;
        }
        
        return dfs(node.left, num) + dfs(node.right, num);
    };
    
    return dfs(root, 0);
};