# Problem: Construct Binary Tree from Inorder and Postorder Traversal
# Difficulty: Medium
# URL: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Runtime: 3 ms
# Memory: 58.4 MB

/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    const map = new Map();
    inorder.forEach((val, idx) => map.set(val, idx));
    
    let postIdx = postorder.length - 1;
    
    const build = (left, right) => {
        if (left > right) return null;
        
        const rootVal = postorder[postIdx--];
        const root = new TreeNode(rootVal);
        const mid = map.get(rootVal);
        
        // Build right subtree first (postorder goes right to left from end)
        root.right = build(mid + 1, right);
        root.left = build(left, mid - 1);
        
        return root;
    };
    
    return build(0, inorder.length - 1);
};