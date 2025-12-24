# Problem: Path Sum II
# Difficulty: Medium
# URL: https://leetcode.com/problems/path-sum-ii/
# Runtime: 1 ms
# Memory: 58.6 MB

/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number[][]}
 */
var pathSum = function(root, targetSum) {
    const result = [];
    
    const dfs = (node, remaining, path) => {
        if (!node) return;
        
        path.push(node.val);
        
        // Check if leaf node with correct sum
        if (!node.left && !node.right && remaining === node.val) {
            result.push([...path]);
        }
        
        dfs(node.left, remaining - node.val, path);
        dfs(node.right, remaining - node.val, path);
        
        path.pop();
    };
    
    dfs(root, targetSum, []);
    return result;
};